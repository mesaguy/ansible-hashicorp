import os


import pytest


if os.getenv('HASHICORP_SOFTWARE_NAMES') is None:
    SOFTWARE_NAMES = [
        'boundary',
        'consul',
        'envconsul',
        'nomad',
        'packer',
        'sentinel',
        'serf',
        'terraform',
        'vagrant',
        'vault',
        'vault-ssh-helper',
        'waypoint',
    ]
else:
    SOFTWARE_NAMES = os.getenv('HASHICORP_SOFTWARE_NAMES').split(',')


def check_binary_symlink(binary_file, dest_path):
    assert binary_file.exists
    assert binary_file.is_symlink
    assert binary_file.user == 'root'
    assert binary_file.group in ('staff', 'root')
    binary_file.linked_to == dest_path


def software_base_directory(hashicorp_dir, name):
    return f'{hashicorp_dir}/{name}'


def software_version(hashicorp_versions, name):
   safe_name = name.replace("-", "_")
   assert safe_name in hashicorp_versions
   return hashicorp_versions[safe_name]


@pytest.mark.parametrize('name', SOFTWARE_NAMES)
def test_software_base_dir(name, host, hashicorp_dir, hashicorp_versions):
    dir_base = software_base_directory(hashicorp_dir, name)
    version = software_version(hashicorp_versions, name)
    directory = host.file(dir_base)
    assert directory.exists
    assert directory.is_directory
    assert directory.group == 'root'
    assert directory.user == 'root'
    assert directory.mode == 0o755
    # Contains two directories, "active" and the current version
    directory_list = directory.listdir()
    assert 'active' in directory_list
    assert version in directory_list
    assert len(directory.listdir()) == 2, f'Directories: {directory_list}'


@pytest.mark.parametrize('name', SOFTWARE_NAMES)
def test_software_version_dir(name, host, hashicorp_dir, hashicorp_versions):
    dir_base = software_base_directory(hashicorp_dir, name)
    version = software_version(hashicorp_versions, name)
    dir_version = f'{dir_base}/{version}'
    directory = host.file(dir_version)
    assert directory.exists
    assert directory.is_directory
    assert directory.group == 'root'
    assert directory.user == 'root'
    assert directory.mode == 0o755
    # Contains just one file, the binary
    assert len(directory.listdir()) == 1


@pytest.mark.parametrize('name', SOFTWARE_NAMES)
def test_software_binary(name, host, hashicorp_dir, hashicorp_versions):
    dir_base = software_base_directory(hashicorp_dir, name)
    version = software_version(hashicorp_versions, name)
    binary_file_path = f'{dir_base}/{version}/{name}'
    binary_file = host.file(binary_file_path)
    assert binary_file.exists
    assert binary_file.is_file
    assert binary_file.group == 'root'
    assert binary_file.user == 'root'
    assert binary_file.mode == 0o755
    assert binary_file.size > 10000


@pytest.mark.parametrize('name', SOFTWARE_NAMES)
def test_software_binary_symlink(name, host, binary_symlink_dir, hashicorp_dir,
                                 hashicorp_versions):
    dir_base = software_base_directory(hashicorp_dir, name)
    version = software_version(hashicorp_versions, name)
    dest_path = f'{dir_base}/{version}/{name}'
    symlink_file = host.file(f'{binary_symlink_dir}/{name}')
    assert symlink_file.exists
    assert symlink_file.is_symlink
    assert symlink_file.group in ('staff', 'root')
    assert symlink_file.user == 'root'
    symlink_file.linked_to == dest_path


@pytest.mark.parametrize('name', SOFTWARE_NAMES)
def test_software_active_dir_symlink(name, host, hashicorp_dir, hashicorp_versions):
    dir_base = software_base_directory(hashicorp_dir, name)
    version = software_version(hashicorp_versions, name)
    dest_path = f'{dir_base}/{version}'
    active_symlink = host.file(f'{dir_base}/active')
    assert active_symlink.exists
    assert active_symlink.is_symlink
    assert active_symlink.user == 'root'
    assert active_symlink.group in ('staff', 'root')
    active_symlink.linked_to == dest_path
