/* Read : & */
fn calculate_length(s: & String) -> usize {

    s.len()

}


/* Write : &mut */
fn change(s: &mut String) {

    s.push_str(" World !")

}

fn main() {

    let mut s1 = String::from("hello");

    let mut len = calculate_length(&s1);

    println!("la longueur est {}", len);

    change(&mut s1);
    
    len = calculate_length(&s1);
    
    println!("la longueur est {}", len);
}
