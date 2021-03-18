import os


def test_installed(host):
    if os.environ['MOLECULE_DISTRO'] == 'archlinux':
        for name in (
                'consul',
                'packer',
                'terraform',
                'vagrant',
                'vault',
            )
            assert host.package(name).is_installed
    elif os.environ['MOLECULE_DISTRO'] == 'gentoo':
        for name in (
                'app-admin/consul',
                'sys-cluster/nomad',
                'dev-util/packer',
                'app-admin/terraform',
                'app-emulation/vagrant',
                'app-admin/vault',
            )
            assert host.package(name).is_installed
    else:
        assert False, 'No tests defined'
