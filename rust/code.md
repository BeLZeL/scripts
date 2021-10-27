#------------------------------------------------------------------------------
# Basics

let : pour définir une constante
let mut : pour définir une variable

println!("") : pour afficher quelque chose
    println!("hello world");

fn : pour définir une fonction/méthode
    fn is_naked(&self) -> bool { 
        self.naked 
    }

fn main() : la fonction de base 
    fn main() { 
    }

impl : pour implémenter une nouvelle classe
    impl Sheep { 
        fn new(name: &'static str) -> Sheep { 
            Sheep { name: name, naked: false } 
        } 

struct : pour créer rapidement une structure de données
pub struct ConnInfo {
    pub name: String,
    pub host: String,
    pub port: u16,
}
let db_params = ConnInfo {
    name: "mydb",
    host: "localhost",
    port: 5432
};

# https://doc.rust-lang.org/rust-by-example/flow_control/for.html
# 1, 2, 3, 4, 5
for y in 1..=5
# 1, 2, 3, 4
for y in 1..5

# Trait : https://doc.rust-lang.org/rust-by-example/trait.html
Un trait est un agrégat de méthodes définies pour un type inconnu : Self. Elles peuvent accéder aux autres méthodes déclarées dans le même trait. Les traits peuvent être implémentés pour n'importe quel type de donnée. Dans l'exemple ci-dessous, nous définissons Animal, un groupe de méthodes. Le trait Animal est alors implémenté pour le type Sheep, permettant l'utilisation des méthodes de Animal avec une instance du type Sheep.

#------------------------------------------------------------------------------
# Convert


#------------------------------------------------------------------------------
# https://doc.rust-lang.org/std/string/struct.String.html
# Empty string
let mut chaine = String::new();
let mut chaine = String::from("");
let mut chaine = "".to_string();

# Concatene string
chaine += &"X".to_string();




