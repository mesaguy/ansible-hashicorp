import pytest


@pytest.fixture(scope='module')
def binary_symlink_dir():
    return '/usr/local/bin'


@pytest.fixture(scope='module')
def hashicorp_dir():
    return '/opt/hashicorp'


def ansible_facts(host):
    setup = host.ansible("setup")["ansible_facts"]
    assert 'ansible_facts' in setup
    return setup["ansible_facts"]


@pytest.fixture(scope='module')
def hashicorp_versions(host):
    version_vars = host.ansible("include_vars", "file=vars/versions.yml")
    assert 'ansible_facts' in version_vars
    versions = version_vars['ansible_facts']
    assert versions
    return versions


@pytest.fixture(scope='module')
def hashicorp_official_package_names(host):
    names_vars = host.ansible("include_vars", "file=vars/main.yml")
    assert 'ansible_facts' in names_vars
    names = names_vars['ansible_facts']['hashicorp_official_package_names']
    assert names
    return names


@pytest.fixture(scope='module')
def hashicorp_package_names(host):
    names_vars = host.ansible("include_vars", "file=vars/main.yml")
    assert 'ansible_facts' in names_vars
    names = names_vars['ansible_facts']['hashicorp_package_names']
    assert names
    return names
