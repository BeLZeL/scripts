/* Read : & */
fn calculate_length(s: &String) -> usize {
    s.len()
}

/* Write : &mut */
fn change(s: &mut String) {
    s.push_str(" World !")
}

fn main() {
    let mut s1 = String::from("hello");
    for char in s1.chars() {
        println!("{}", char); // show h e l l o
    }

    let mut len = calculate_length(&s1);
    println!("la longueur est {}", len); // show 5

    change(&mut s1);
    len = calculate_length(&s1);
    println!("la longueur est {}", len); // show 13

    let slice = &s1[6..];
    println!("la fin est '{}'", slice); // show "World !"
}
