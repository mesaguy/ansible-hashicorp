def test_installed_software(host):
    assert host.package("consul").is_installed or \
        host.file('/usr/local/bin/consul').is_file
    nomad_package = host.package("nomad")
    if nomad_package.is_installed:
        assert nomad_package.version == '1.0.0'
    else:
        assert host.file('/usr/local/bin/nomad').is_file
    assert host.package("terraform").is_installed or \
        host.file('/usr/local/bin/terraform').is_file

def test_nomad_version(host):
    cmd = host.run('nomad --version')
    assert cmd.rc == 0
    assert 'Nomad v1.0.0' in cmd.stdout
