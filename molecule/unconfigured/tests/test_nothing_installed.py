def test_base_directory_missing(host):
   directory = host.file('/opt/hashicorp')
   assert not directory.exists
