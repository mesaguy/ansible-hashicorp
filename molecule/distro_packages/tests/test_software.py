import os


def test_installed(host):
    assert os.environ['IMAGE_DISTRO'], '"IMAGE_DISTRO" env var must be set'
    assert os.environ['IMAGE_TAG'], '"IMAGE_TAG" env var must be set'
    if os.environ['IMAGE_DISTRO'] == 'archlinux':
        for name in (
                'consul',
                'packer',
                'terraform',
                'vagrant',
                'vault',
            ):
            assert host.package(name).is_installed
    elif os.environ['IMAGE_DISTRO'] == 'gentoo':
        world = host.file('/var/lib/portage/world')
        for name in (
                'app-admin/consul',
                'sys-cluster/nomad',
                'dev-util/packer',
                'app-admin/terraform',
                #'app-emulation/vagrant',
                'app-admin/vault',
            ):
            assert name in world.content_string
            # As of 20210414, TestInfra doesn't support checking software
            # installed on Gentoo
            #assert host.package(name).is_installed
    else:
        assert False, 'No tests defined'
