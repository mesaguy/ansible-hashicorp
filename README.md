# Ansible HashiCorp

Installs and updates the following [HashiCorp](https://www.hashicorp.com) software:

- Boundary
- Consul
- EnvConsul
- Nomad
- Packer
- Sentinel
- Serf
- Terraform
- Vagrant
- Vault
- Vault SSH Helper
- Waypoint

This role may eventually manage some [HashiCorp](https://www.hashicorp.com) software, but the current focus is exclusively the installation of [HashiCorp](https://www.hashicorp.com) software in a secure, consistent, and reproducible manner.

## Requirements

- Ansible >= 2.9.0
- Facts must be gathered (gather_facts: true)

## Role Variables

By default, this role installs no software. Each piece of software must be specifically enabled.

The following variables can be defined to install specific HashiCorp software:

    hashicorp_install_boundary: true
    hashicorp_install_consul: true
    hashicorp_install_envconsul: true
    hashicorp_install_nomad: true
    hashicorp_install_packer: true
    hashicorp_install_sentinel: true
    hashicorp_install_serf: true
    hashicorp_install_terraform: true
    hashicorp_install_vagrant: true
    hashicorp_install_vault: true
    hashicorp_install_vault_ssh_helper: true
    hashicorp_install_waypoint: true

By default, software is installed to this base directory. For instance, the consul version 1.0.0 binary would be installed to /opt/hashicorp/consul/1.0.0/consul

    hashicorp_base_dir: /opt/hashicorp

Symlinks to each binary are created here:

    hashicorp_software_link_dir: /usr/local/bin

Validate the GPG signatures on all binaries (default: false). This requires the "gpg" command to be available. If the HashiCorp GPG release public key is missing, this role will automatically add the GPG public key to the "root" users GPG keyring:

   hashicorp_check_gpg_signatures: true

Purge all except the latest software release (default: false):

    hashicorp_purge_old_releases: true


Change the user who owns the software, defaults to the options below:

    hashicorp_user: root
    hashicorp_group: root

If a local mirror of the HashiCorp software is available, you can "HASHICORP_MIRROR" and/or "HASHICORP_GPG_MIRROR" environmental variables or the following ansible variables. The "hashicorp_gpg_mirror" variable only affects where GPG signature files are sourced:

   hashicorp_mirror: https://example.org/hashicorp
   hashicorp_gpg_mirror: https://example.org/hashicorp

## Dependencies

N/A

## Example Playbook


The following example would install 'Consul' and 'Vault' software:

    - hosts: servers
      vars:
        hashicorp_install_consul: true
        hashicorp_install_vault: true
      roles:
         - { role: mesaguy.hashicorp }

## Release management
### Updating default software versions

Default software release versions are controlled by the 'vars/versions.yml' and 'docker_versions.yml' files.

These files can be updated manually or by running the ```scripts/update_versions``` script.

### Testing
Tests are run via molecule.

You will need [pipenv](https://pipenv.pypa.io) installed and [docker](https://www.docker.com) running in order to test.

Initialize the pipenv environment by running the following in the base directory of this repo:

    pipenv install

The following can be used for basic validation. The first tests a normal install and the second scenario ensures GPG validation works:

    MOLECULE_DISTRO=debian MOLECULE_TAG=debian-10 pipenv run molecule test
    MOLECULE_DISTRO=debian MOLECULE_TAG=debian-10 pipenv run molecule test -s gpg

## License

MIT
See the [LICENSE](https://github.com/mesaguy/ansible-hashicorp/blob/master/LICENSE) file

## Author Information

Mesaguy
 - https://github.com/mesaguy
