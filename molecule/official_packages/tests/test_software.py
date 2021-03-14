def test_installed(host, hashicorp_official_package_names):
    for name in hashicorp_official_package_names:
        assert host.package(name).is_installed
