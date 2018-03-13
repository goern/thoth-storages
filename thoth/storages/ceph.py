"""Adapter for Ceph distributed object storage."""

import json
import os
import typing

import boto3
import botocore

from .base import StorageBase


class CephStore(StorageBase):
    """Adapter for storing analysis results."""

    def __init__(self, result_type, *,
                 host: str=None, key_id: str=None, secret_key: str=None, bucket: str=None, region: str=None):
        super().__init__()
        self.deployment_name = os.environ['THOTH_DEPLOYMENT_NAME']
        self.host = host or os.environ['THOTH_CEPH_HOST']
        self.key_id = key_id or os.environ['THOTH_CEPH_KEY_ID']
        self.secret_key = secret_key or os.environ['THOTH_CEPH_SECRET_KEY']
        self.bucket = bucket or os.environ['THOTH_CEPH_BUCKET']
        self.region = region or os.getenv('THOTH_CEPH_REGION', None)
        self.result_type = result_type
        self._s3 = None

        assert self.result_type, "Result type cannot be empty: {}".format(self.result_type)
        assert self.deployment_name, "Deployment name has to be set, got {}".format(self.deployment_name)

        self.prefix = "{}/{}".format(self.deployment_name, self.result_type)

    def get_document_listing(self) -> typing.Generator[str, None, None]:
        """Get listing of documents stored on the Ceph."""
        for obj in self._s3.Bucket(self.bucket).objects.filter(Prefix=self.prefix).all():
            yield obj.key[len(self.prefix):]

    @staticmethod
    def _dict2blob(dictionary: dict) -> bytes:
        """Encode a dictionary to a blob so it can be stored on Ceph."""
        return json.dumps(dictionary, sort_keys=True, separators=(',', ': '), indent=2).encode()

    def _store_blob(self, blob: bytes, object_key: str) -> dict:
        """Store a blob on Ceph."""
        put_kwargs = {'Body': blob}
        object_path = "{}/{}".format(self.prefix, object_key)
        response = self._s3.Object(self.bucket, object_path).put(**put_kwargs)
        return response

    def store_document(self, document: dict, document_id: str) -> dict:
        """Store a document (dict) onto Ceph."""
        blob = self._dict2blob(document)
        return self._store_blob(blob, document_id)

    def _retrieve_blob(self, object_key: str) -> bytes:
        """Retrieve remote object content."""
        object_path = "{}/{}".format(self.prefix, object_key)
        return self._s3.Object(self.bucket, object_path).get()['Body'].read()

    def retrieve_document(self, document_id: str) -> dict:
        """Retrieve a dictionary stored as JSON from S3."""
        return json.loads(self._retrieve_blob(document_id).decode())

    def is_connected(self) -> bool:
        """Check whether adapter is already connected to the remote Ceph storage."""
        return self._s3 is not None

    def document_exists(self, document_id: str) -> bool:
        """Check if the there is an object with the given key in bucket, does only HEAD request."""
        object_path = "{}/{}".format(self.prefix, document_id)
        try:
            self._s3.Object(self.bucket, object_path).load()
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                exists = False
            else:
                raise
        else:
            exists = True
        return exists

    def connect(self) -> None:
        """Create a connection to the remote Ceph."""
        session = boto3.session.Session(aws_access_key_id=self.key_id,
                                        aws_secret_access_key=self.secret_key,
                                        region_name=self.region)
        # signature version is needed to connect to new regions which support only v4
        self._s3 = session.resource(
            's3',
            config=botocore.client.Config(signature_version='s3v4'),
            endpoint_url=self.host
        )
        self._create_bucket_if_needed()

    def _create_bucket_if_needed(self) -> None:
        """Create desired bucket based on configuration if the given bucket does not already exist."""
        # check that the bucket exists - see boto3 docs
        try:
            self._s3.meta.client.head_bucket(Bucket=self.bucket)
        except botocore.exceptions.ClientError as exc:
            # if a client error is thrown, then check that it was a 404 error.
            # if it was a 404 error, then the bucket does not exist.
            try:
                error_code = int(exc.response['Error']['Code'])
            except (TypeError, ValueError, KeyError):
                raise
            if error_code == 404:
                self._create_bucket()
            else:
                raise

    def _create_bucket(self) -> None:
        """Create a bucket."""
        # Yes boto3, you are doing it right:
        #   https://github.com/boto/boto3/issues/125
        if self.region == 'us-east-1':
            self._s3.create_bucket(Bucket=self.bucket)
        else:
            self._s3.create_bucket(
                Bucket=self.bucket,
                CreateBucketConfiguration={
                    'LocationConstraint': self.region
                }
            )
