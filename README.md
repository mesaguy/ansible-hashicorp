# Ansible HashiCorp
![Molecule tests](https://github.com/mesaguy/ansible-hashicorp/actions/workflows/test.yml/badge.svg) ![Latest tag](https://img.shields.io/github/v/tag/mesaguy/ansible-hashicorp) ![Ansible Galaxy](https://img.shields.io/badge/ansible%20galaxy-mesaguy.hashicorp-blue.svg?style=flat) ![MIT License](https://img.shields.io/github/license/mesaguy/ansible-hashicorp)

Install [HashiCorp](https://www.hashicorp.com) software using official packages, official zip files, and distro packages.

Installs and updates the following [HashiCorp](https://www.hashicorp.com) software:

- Boundary
- Consul
- Consul Template
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

### Generic

By default, this role installs no software. Each piece of software must be specifically enabled.

The following variables can be defined to install specific HashiCorp software:

    hashicorp_install_boundary: true
    hashicorp_install_consul: true
    hashicorp_install_consul_template: true
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

Alternatively, HashiCorp software can be specified using the "hashicorp_install" variable when calling this role. When "hashicorp_install" is specified, the hashicorp_install_\* variables above will be ignored. This syntax also supports optionally specifying a version:

    - name: Include mesaguy.hashicorp to install specific software
      include_role:
        name: mesaguy.hashicorp
      vars:
        hashicorp_install:
          # Install Consul version 1.0.0
          - consul==1.0.0
          # Install the latest versions of packer and vault
          - packer
          - vault

### HashiCorp ZIP file installs

By default, this role installs HashiCorp's ZIP files containing pre-compiled binaries using the variables below

Software is installed to this base directory. For instance, the consul version 1.0.0 binary would be installed to /opt/hashicorp/consul/1.0.0/consul

    hashicorp_base_dir: /opt/hashicorp

Symlinks to each binary are created here:

    hashicorp_software_link_dir: /usr/local/bin

Validate the GPG signatures on all release ZIP files (default: false). This requires the "gpg" command to be available. If the HashiCorp GPG release public key is missing, this role will automatically add the GPG public key to the "root" users GPG keyring:

   hashicorp_check_gpg_signatures: true

Purge all except the latest software release (default: false):

    hashicorp_purge_old_releases: true

Change the user who owns the software, defaults to the options below:

    hashicorp_user: root
    hashicorp_group: root

If a local mirror of the HashiCorp software is available, you can "HASHICORP_MIRROR" and/or "HASHICORP_GPG_MIRROR" environmental variables or the following ansible variables. The "hashicorp_gpg_mirror" variable only affects where GPG signature files are sourced:

   hashicorp_mirror: https://example.org/hashicorp
   hashicorp_gpg_mirror: https://example.org/hashicorp

### Use HashiCorp packages instead of ZIP files

When enabled, use HashiCorp's official RPM/DEB packages instead of HashiCorp's official ZIP files, defaults to false:

    hashicorp_use_official_packages: true

This option applies to the following distro releases and architectures:

| Distro      | Release        | Architectures |
|-------------|----------------|---------------|
| AmazonLinux | 2              | amd64/x86_64  |
| Debian      | Jessie (8)     | amd64/x86_64  |
| Debian      | Stretch (9)    | amd64/x86_64  |
| Debian      | Buster (10)    | amd64/x86_64  |
| Fedora      | 29             | amd64/x86_64  |
| Fedora      | 30             | amd64/x86_64  |
| Fedora      | 31             | amd64/x86_64  |
| Fedora      | 32             | amd64/x86_64  |
| Fedora      | 33             | amd64/x86_64  |
| RHEL        | 7              | amd64/x86_64  |
| RHEL        | 8              | amd64/x86_64  |
| Ubuntu      | Bionic (18.04) | amd64/x86_64  |
| Ubuntu      hashicorp_use_official_packages:| Eoam (19.10)   | amd64/x86_64  |
| Ubuntu      | Focal (20.04)  | amd64/x86_64  |
| Ubuntu      | Groovy (20.10) | amd64/x86_64  |
| Ubuntu      | Xenial (16.04) | amd64/x86_64  |

Purge HashiCorp software installed via ZIP files, defaults to false:

    hashicorp_purge_zip_releases: true

A local apt mirror can be specified using the "hashicorp_apt_mirror" ansible variable or "HASHICORP_APT_MIRROR" environmental variable:

    hashicorp_apt_mirror: https://example.org/hashicorp/apt

A local yum mirror can be specified using the "hashicorp_yum_mirror" ansible variable or "HASHICORP_YUM_MIRROR" environmental variable:

    hashicorp_yum_mirror: https://example.org/hashicorp/yum

State to keep HashiCorp software in, defaults to "present":

    hashicorp_software_state: latest

When install HashiCorp's binary zip files, software version using the following syntax:

    hashicorp_nomad_version: 1.0.1
    hashicorp_vault_version: 1.0.1


### Use Distro packages instead of ZIP files

When enabled, use the distro's (potentially unofficial) packages instead of HashiCorp's official ZIP files, defaults to false:

    hashicorp_use_distro_packages: true

Currently, this option applies to ArchLinux only

Purge HashiCorp software installed via ZIP files, defaults to false:

    hashicorp_purge_zip_releases: true

The yum testing repository can be enabled via:

    hashicorp_enable_yum_test_repo: true

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

    IMAGE_DISTRO=debian IMAGE_TAG=debian-10 pipenv run molecule test
    IMAGE_DISTRO=debian IMAGE_TAG=debian-10 pipenv run molecule test -s gpg

Selinux errors can generally be solved with:

    pipenv run pip uninstall selinux -y; pipenv install

## License

MIT
See the [LICENSE](https://github.com/mesaguy/ansible-hashicorp/blob/master/LICENSE) file

## Author Information

Mesaguy
 - https://github.com/mesaguy
