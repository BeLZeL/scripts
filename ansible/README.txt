#------------------------------------------------------------------------------
# Debian jessie
$ aptitude install -t jessie-backports ansible

$ ansible-playbook --version
ansible-playbook 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides

#------------------------------------------------------------------------------
# Documentation :
http://docs.ansible.com/ansible/latest/modules_by_category.html
http://docs.ansible.com/ansible/latest/list_of_files_modules.html
https://nsrc.org/workshops/2015/rwnog/raw-attachment/wiki/Track2Agenda/first-playbook.htm

#------------------------------------------------------------------------------
# /etc/ansible/hosts
$ ansible-playbook -i "localhost," -c local helloworld.yml
$ vim /etc/ansible/hosts
localhost ansible_connection=local
$ ansible-playbook helloworld.yml
$ ansible all -m shell -a 'echo hello world'