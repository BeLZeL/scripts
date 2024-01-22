use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn read_int() -> Result<i32, std::num::ParseIntError> {
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read line");
    buffer.trim().parse::<i32>()
}

fn main() {
    println!("Guess the number!");
    let secret_number = rand::thread_rng().gen_range(1..101);
    println!("The secret number is: {}", secret_number);
    println!("Please input your guess.");

    loop {
        match read_int() {
            Ok(number) => {
                match number.cmp(&secret_number) {
                    Ordering::Less => println!("Too small!"),
                    Ordering::Greater => println!("Too big!"),
                    Ordering::Equal => { println!("You win!"); break },
                }
            }
            Err(_) => {
                println!("Error : invalid integer.");
            }
        }
    }
}
