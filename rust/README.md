Pour installer et utiliser rust : https://rustup.rs/
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Il y a des fichiers installés dans ~/.cargo et ~/.rustup.

Pour mettre à jour : https://www.rust-lang.org/learn/get-started
$ rustup update

Initier un nouveau projet :
$ cargo new hello-rust


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


# -----------------------------------------------------------------------------
# Install crate

vagrant@stretch:~$ cargo install postgres
    Updating crates.io index
  Downloaded postgres v0.15.2
  Downloaded 1 crate (25.1 KB) in 1.97s
error: specified package `postgres v0.15.2` has no binaries


# -----------------------------------------------------------------------------
# Cargo

$ cargo new hello_cargo
     Created binary (application) `hello_cargo` package
$ cd hello_cargo
$ cat src/main.rs 
fn main() {
    println!("Hello, world!");
}

$ cargo build
   Compiling hello_cargo v0.1.0 (/sshfs/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 1.33s

$ ./target/debug/hello_cargo 
Hello, world!


# -----------------------------------------------------------------------------
# Tutorials / Links
https://parallel-rust-cpp.github.io/introduction.html
