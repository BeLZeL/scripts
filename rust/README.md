Pour installer et utiliser rust : https://rustup.rs/


# -----------------------------------------------------------------------------
# Préparation d'une VM Debian Stretch (~/rust) :

$ cat Vagrantfile 
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "stretch64"
    #config.vm.synced_folder ".", "/vagrant", type: "nfs", disabled: false
    config.vm.synced_folder ".", "/sshfs", type: "sshfs"

    # This block solves some performance issues
    config.vm.provider "virtualbox" do |v|
        v.linked_clone = true
        v.memory = 512
        v.cpus = 2
        v.customize [ "storagectl", :id, "--name", "SATA Controller", "--hostiocache", "off" ]
    end
end

$ vagrant up
$ vagrant ssh


# -----------------------------------------------------------------------------
# Dans la VM Debian Stretch :

$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
[...]
   default host triple: x86_64-unknown-linux-gnu
     default toolchain: stable
  modify PATH variable: yes
1) Proceed with installation (default)

Then :
https://www.tecmint.com/install-rust-programming-language-in-linux/

Then :
sudo aptitude install gcc

Then :
https://doc.rust-lang.org/stable/book/

Tuto :
https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMF-221/Les-langages-de-demain
https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMF-185/Apprenez-RUST-et-appuyez-sur-le-champignon

for :
https://doc.rust-lang.org/rust-by-example/flow_control/for.html


# -----------------------------------------------------------------------------
# Hello World

~/rust/001_hello_world$ cat main.rs 
fn main() {
    println!("Hello World !");
}

vagrant@stretch:~/sshfs/001_hello_world$ rustc main.rs 

~/rust/001_hello_world$ ./main 
Hello World !
