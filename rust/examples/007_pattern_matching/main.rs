fn main() {

    for i in 1..=101 {
        match i {
            x @ 50 ..= 100 => println!("{} est entre 50 et 100", x),
            11 | 12 => println!("{} est égal à 11 ou 12", i),
            _ => println!("{} n'est ni 11, ni 12, ni entre 50 et 100", i),
        }
    }
    
    
    // FizzBuzz
    for n in 1..=100 {
    
        match (n % 3, n % 5) {
            (0, 0) => println!("fizzbuzz"),
            (0, _) => println!("fizz"),
            (_, 0) => println!("buzz"),
            _ => println!("{}", n)
        }
    }
    
    
    // https://stackoverflow.com/questions/25383488/how-to-match-a-string-against-string-literals
    let stringthing = String::from("c");
    
    match &stringthing[..] {
        "a" => println!("0"),
        "b" => println!("1"),
        "c" => println!("2"), // <-------
        _ => println!("something else!"),
    }

    match stringthing.as_str() {
        "a" => println!("0"),
        "b" => println!("1"),
        "c" => println!("2"), // <-------
        _ => println!("something else!"),
    }

    match stringthing.as_ref() {
        "a" => println!("0"),
        "b" => println!("1"),
        "c" => println!("2"), // <-------
        _ => println!("something else!"),
    }

}
