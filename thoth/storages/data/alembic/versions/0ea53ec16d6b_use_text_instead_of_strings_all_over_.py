"""Use Text instead of Strings all over the place

Revision ID: 0ea53ec16d6b
Revises: 125a71b49a50
Create Date: 2020-03-25 08:21:13.153294+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ea53ec16d6b'
down_revision = '125a71b49a50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('adviser_run', 'adviser_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('adviser_run', 'adviser_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('adviser_run', 'adviser_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('adviser_run', 'origin',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('adviser_run', 're_run_adviser_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('cve', 'advisory',
               existing_type=sa.VARCHAR(length=16384),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('cve', 'cve_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('cve', 'cve_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('cve', 'version_range',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('deb_dependency', 'package_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('deb_depends', 'version_range',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('deb_package_version', 'arch',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('deb_package_version', 'epoch',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('deb_package_version', 'package_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('deb_package_version', 'package_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('deb_pre_depends', 'version_range',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('deb_replaces', 'version_range',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'decision',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('depends_on', 'version_range',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('ecosystem_solver', 'ecosystem',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'os_name',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'os_version',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'python_version',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'solver_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'solver_version',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('external_hardware_information', 'cpu_model_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_hardware_information', 'gpu_model_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_hardware_information', 'gpu_vendor',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'cuda_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'environment_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'image_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'image_sha',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'os_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'python_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('found_python_file', 'file',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('hardware_information', 'cpu_model_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('hardware_information', 'gpu_model_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('hardware_information', 'gpu_vendor',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('included_file', 'file',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('inspection_run', 'amun_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('inspection_run', 'inspection_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_analyzer_run', 'package_analysis_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_analyzer_run', 'package_analyzer_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('package_analyzer_run', 'package_analyzer_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('package_extract_run', 'analysis_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'image_tag',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'origin',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('package_extract_run', 'os_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'os_version_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'package_extract_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'package_extract_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'origin',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('provenance_checker_run', 'provenance_checker_document_id',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'provenance_checker_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'provenance_checker_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_artifact', 'artifact_hash_sha256',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_artifact', 'artifact_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('python_file_digest', 'sha256',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_interpreter', 'link',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('python_interpreter', 'path',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_interpreter', 'version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('python_package_index', 'url',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_index', 'warehouse_api_url',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('python_package_requirement', 'name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_requirement', 'version_range',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version', 'os_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version', 'package_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version', 'package_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('python_package_version', 'python_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version_entity', 'package_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('python_package_version_entity', 'package_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('rpm_package_version', 'arch',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('rpm_package_version', 'epoch',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('rpm_package_version', 'package_identifier',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'package_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'package_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'release',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('rpm_requirement', 'rpm_requirement_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('software_environment', 'cuda_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'environment_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'image_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'image_sha',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'os_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('software_environment', 'python_version',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('solved', 'document_id',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('versioned_symbol', 'library_name',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('versioned_symbol', 'symbol',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('versioned_symbol', 'symbol',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('versioned_symbol', 'library_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('solved', 'document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('software_environment', 'python_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'os_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'os_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'image_sha',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'image_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'environment_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('software_environment', 'cuda_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('rpm_requirement', 'rpm_requirement_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'release',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('rpm_package_version', 'package_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'package_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'package_identifier',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('rpm_package_version', 'epoch',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('rpm_package_version', 'arch',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_package_version_entity', 'package_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_package_version_entity', 'package_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_version', 'python_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_version', 'package_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_package_version', 'package_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_version', 'os_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_version', 'os_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_requirement', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_requirement', 'name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_package_index', 'warehouse_api_url',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_package_index', 'url',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_interpreter', 'version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_interpreter', 'path',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_interpreter', 'link',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_file_digest', 'sha256',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('python_artifact', 'artifact_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('python_artifact', 'artifact_hash_sha256',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'provenance_checker_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'provenance_checker_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'provenance_checker_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('provenance_checker_run', 'origin',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('package_extract_run', 'package_extract_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'package_extract_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'os_version_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'os_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'os_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'origin',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('package_extract_run', 'image_tag',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_extract_run', 'analysis_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('package_analyzer_run', 'package_analyzer_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('package_analyzer_run', 'package_analyzer_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('package_analyzer_run', 'package_analysis_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('inspection_run', 'inspection_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('inspection_run', 'amun_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('included_file', 'file',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('hardware_information', 'gpu_vendor',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('hardware_information', 'gpu_model_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('hardware_information', 'cpu_model_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('found_python_file', 'file',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('external_software_environment', 'python_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'os_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'os_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'image_sha',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'image_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'environment_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_software_environment', 'cuda_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_hardware_information', 'gpu_vendor',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_hardware_information', 'gpu_model_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('external_hardware_information', 'cpu_model_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('ecosystem_solver', 'solver_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'solver_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'python_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=8),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'os_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=8),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'os_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('ecosystem_solver', 'ecosystem',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('depends_on', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'dependency_monkey_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('dependency_monkey_run', 'decision',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    op.alter_column('deb_replaces', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('deb_pre_depends', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('deb_package_version', 'package_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('deb_package_version', 'package_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('deb_package_version', 'epoch',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('deb_package_version', 'arch',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('deb_depends', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('deb_dependency', 'package_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('cve', 'version_range',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('cve', 'cve_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('cve', 'cve_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('cve', 'advisory',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=16384),
               existing_nullable=True)
    op.alter_column('adviser_run', 're_run_adviser_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('adviser_run', 'origin',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=True)
    op.alter_column('adviser_run', 'adviser_version',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('adviser_run', 'adviser_name',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    op.alter_column('adviser_run', 'adviser_document_id',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)
    # ### end Alembic commands ###
