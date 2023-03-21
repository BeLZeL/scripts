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

https://connect.ed-diamond.com/linux-pratique/lphs-054/les-bases-de-l-automatisation-a-l-aide-d-ansible
https://connect.ed-diamond.com/linux-pratique/lphs-054/allez-plus-loin-avec-ansible-a-l-aide-de-ses-collections
https://connect.ed-diamond.com/linux-pratique/lphs-054/creer-une-collection-pour-ansible
https://connect.ed-diamond.com/linux-pratique/lphs-054/conception-d-un-module-pour-ansible

#------------------------------------------------------------------------------

Termes :
* Contrôleur : machine qui va exécuter ansible
* Cible : machine qui sera impactée par ansible
* Inventaire : liste des cibles
* Rôle : contenu réutilisable ($ mkdir -p roles/nginx/{defaults,files,handlers,tasks,templates,vars})
    ├── defaults : valeurs par défaut des variables (public) (voir vars)
    ├── files : fichiers statiques (déployés tels quels sur la cible) (voir templates)
    ├── handlers : actions à entreprendre lors de la notification d’événements (redémarrer un service après un changement de conf)
    ├── README.md
    ├── tasks : playbooks
    ├── templates : fichiers dynamiques (déployés sur la cible) (voir files)
    └── vars : valeurs par défaut des variables (private) (voir defaults)

#------------------------------------------------------------------------------
# /etc/ansible/hosts
$ ansible-playbook -i "localhost," -c local helloworld.yml
$ vim /etc/ansible/hosts
localhost ansible_connection=local
$ ansible-playbook helloworld.yml
$ ansible all -m shell -a 'echo hello world'

#------------------------------------------------------------------------------

Voir les variables récupérables par Ansible :
$ ansible -m setup localhost

Désactiver la récupération couteuse de ces variables, dans le yaml :
gather_facts: false

Vérification syntaxique :
$ ansible-playbook --syntax-check playbook.yml

#------------------------------------------------------------------------------

Exemple pour tasks et handlers :

roles/nginx/tasks/main.yml : 
- name: ...
  [...]
  notify:
    - Restart Nginx
    
roles/nginx/handlers/main.yml :
  - name: Restart Nginx
    ansible.builtin.service:
      name: nginx
      state: restarted
