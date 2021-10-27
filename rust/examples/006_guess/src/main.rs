use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {

    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();

 
 /*
    match "foobar".parse::<i32>() {
  Ok(n) => do_something_with(n),
  Err(e) => weep_and_moan(),
}
*/
    
    while true {
    
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
       
        println!("You guessed: {}", guess);

        let myint:i32 = guess.trim().parse().unwrap();
    
        match myint.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }
}
