Pour installer et utiliser rust : https://rustup.rs/
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Il y a des fichiers installés dans ~/.cargo et ~/.rustup.

Pour mettre à jour : https://www.rust-lang.org/learn/get-started
$ rustup update

Initier un nouveau projet :
$ cargo new hello-rust

# -----------------------------------------------------------------------------

Documentation :

    https://doc.rust-lang.org/cargo/commands/cargo-install.html
    https://doc.rust-lang.org/rust-by-example/flow_control/while.html
    https://doc.rust-lang.org/rust-by-example/macros.html
    https://doc.rust-lang.org/rust-by-example/std_misc/channels.html
    https://doc.rust-lang.org/rust-by-example/trait.html
    https://doc.rust-lang.org/std/fmt/trait.Display.html
    https://doc.rust-lang.org/std/ops/trait.Drop.html
    https://doc.rust-lang.org/std/fs/struct.File.html
    
    https://serde.rs/
    https://github.com/serde-rs/serde
    https://docs.serde.rs/serde/index.html
    https://docs.serde.rs/serde_yaml/index.html
    https://blog.rust-lang.org/2021/05/11/edition-2021.html

Rust :
    
    https://blog.rust-lang.org/2022/05/19/Rust-1.61.0.html
    https://blog.rust-lang.org/2021/10/21/Rust-1.56.0.html

Linux Magazine :

    https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMF-245/Rust-le-langage-inoxydable

Developpez.com :

    https://rust.developpez.com/actu/333622/Rust-1-61-0-est-disponible-elle-apporte-de-nouvelles-fonctionnalites-et-ameliorations-plus-de-possibilites-pour-les-const-fn-et-les-manipulations-statiques-pour-stdio-verrouille/
    https://rust.developpez.com/actu/332449/Rust-1-60-0-est-disponible-elle-reactive-la-compilation-incrementale-et-introduit-deux-nouveaux-changements-pour-ameliorer-la-prise-en-charge-des-fonctionnalites-de-Cargo/
    https://rust.developpez.com/actu/331386/Rust-1-59-0-est-disponible-Cette-version-desactive-par-defaut-la-compilation-incrementielle-et-autorise-la-creation-de-binaires-depouilles/
    https://rust.developpez.com/actu/330145/Rust-1-58-est-disponible-avec-la-reduction-du-chemin-de-recherche-sous-Windows-et-etend-les-chaines-de-format-ainsi-que-l-utilisation-de-must-use-dans-la-bibliotheque-standard/
    https://rust.developpez.com/actu/328207/L-edition-Rust-2021-et-la-version-stable-Rust-1-56-sont-maintenant-disponibles-en-telechargement-la-nouvelle-edition-du-langage-inclut-la-prise-en-charge-des-captures-disjointes/
    https://rust.developpez.com/actu/317223/Rust-1-54-est-disponible-Cette-version-vient-etendre-la-connexion-du-langage-a-WebAssembly-et-permet-l-utilisation-de-macros-dans-les-attributs/
    https://rust.developpez.com/actu/316132/Rust-1-53-0-est-disponible-et-s-accompagne-de-IntoIterator-pour-les-tableaux-Cargo-prend-desormais-en-charge-les-referentiels-git-ou-la-branche-HEAD-par-defaut-n-est-pas-master/
    https://rust.developpez.com/actu/313754/Rust-1-51-est-disponible-avec-Resolver-une-nouvelle-fonctionnalite-pour-Cargo-et-l-implementation-MVP-des-const-generics/
    https://rust.developpez.com/actu/312543/Rust-1-50-0-est-disponible-et-s-accompagne-de-l-indexation-de-tableau-generique-Const-ainsi-que-des-affectations-securisees-aux-champs-d-union-ManuallyDrop-lt-T-gt/
    https://rust.developpez.com/actu/311529/Rust-1-49-0-est-disponible-avec-l-amelioration-des-supports-de-Linux-ARM-64-bits-macOS-et-Windows-ARM-64-bits/
    https://rust.developpez.com/actu/310633/Rust-1-48-0-est-disponible-avec-quelques-modifications-dans-rustdoc-pour-rendre-la-redaction-de-documentation-encore-plus-facile/
    https://rust.developpez.com/actu/309518/Rust-1-47-0-est-disponible-et-s-accompagne-de-la-prise-en-charge-par-defaut-de-LLVM-11-ainsi-que-de-neuf-API-qui-passent-en-version-stable-dans-la-bibliotheque/
    https://rust.developpez.com/actu/308326/Rust-1-46-0-est-disponible-et-s-accompagne-de-plusieurs-nouveautes-dans-const-fn-ainsi-que-de-deux-nouvelles-API-dans-la-bibliotheque-standard/
    https://rust.developpez.com/actu/307245/Rust-1-45-0-est-disponible-avec-la-correction-du-probleme-de-la-conversion-entre-des-entiers-et-des-flottants-et-de-nombreuses-fonctionnalites/
    https://rust.developpez.com/actu/305439/Rust-1-44-0-est-disponible-et-apporte-la-commande-cargo-tree-a-Cargo-pour-l-impression-d-un-graphe-arborescent-des-dependances/
    https://rust.developpez.com/actu/301371/Rust-1-43-0-est-disponible-avec-de-nouvelles-API-stabilisees-des-ameliorations-de-performances-du-compilateur-et-une-petite-fonctionnalite-liee-aux-macros/
    https://rust.developpez.com/actu/296960/Rust-1-42-0-Pin-map-unchecked-map-unchecked-mut-ne-necessite-plus-le-type-de-retour-pour-implementer-Sized-Error-description-est-desormais-obsolete/
    https://rust.developpez.com/actu/292032/Rust-1-41-0-est-disponible-et-s-accompagne-de-Cargo-install-qui-met-a-jour-les-packages-lorsqu-ils-sont-obsoletes-et-d-un-format-Cargo-lock-moins-sujet-aux-conflits/
    https://rust.developpez.com/actu/288559/Rust-1-40-est-disponible-Cette-version-s-accompagne-de-non-exhaustive-et-apporte-des-ameliorations-a-macros-et-attribute/
    https://rust.developpez.com/actu/283791/Rust-1-39-0-sonne-l-arrivee-en-version-stable-des-fonctions-async-et-la-possibilite-de-placer-des-attributs-dans-les-parametres-des-fonctions/
    https://rust.developpez.com/actu/278881/Rust-1-38-0-est-disponible-en-version-stable-et-apporte-la-compilation-en-pipeline-et-d-autres-fonctionnalites/
    https://rust.developpez.com/actu/273973/Rust-1-37-0-est-disponible-en-version-stable-et-apporte-des-elements-const-non-nommes-ainsi-qu-une-cle-d-execution-par-defaut-dans-Cargo/
    https://rust.developpez.com/actu/268590/Rust-1-36-0-est-disponible-en-version-stable-et-apporte-le-type-MaybeUninit-lt-T-gt-ainsi-qu-une-nouvelle-implementation-de-HashMap-lt-K-V-gt/
    https://rust.developpez.com/actu/263213/La-version-1-35-0-de-Rust-est-disponible-avec-les-traits-de-fermeture-FnOnce-FnMut-et-Fn-pour-Box-lt-dyn-FnOnce-gt-Box-lt-dyn-FnMut-gt-et-Box-lt-dyn-Fn-gt/
    https://rust.developpez.com/actu/255822/Rust-1-34-0-est-disponible-en-version-stable-et-apporte-le-support-de-l-operateur-dans-les-tests-de-documentation/
    https://www.developpez.com/actu/224880/La-version-stable-de-Rust-1-29-est-desormais-disponible-Premier-jet-de-l-auto-correction-des-lints-et-potentielle-compatibilite-avec-Clippy/
    https://www.developpez.com/actu/165999/Rust-1-21-est-disponible-en-telechargement-le-langage-de-programmation-centre-sur-la-securite-et-la-velocite/
    
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
