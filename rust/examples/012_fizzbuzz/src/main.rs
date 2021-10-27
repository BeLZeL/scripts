fn main() {

    // old-style
    for i in 1 .. 100 {
        if i % 15 == 0 { println!("FizzBuzz") }
        else if i % 3 == 0 { println!("Fizz") }
        else if i % 5 == 0 { println!("Buzz") }
        else { println!("{}", i) }
    }
   
    // pattern matching
    // https://codereview.stackexchange.com/questions/127485/simplest-way-to-write-fizzbuzz-in-rust
    for n in 1..=100 {
    
        match (n % 3, n % 5) {
            (0, 0) => println!("fizzbuzz"),
            (0, _) => println!("fizz"),
            (_, 0) => println!("buzz"),
            _ => println!("{}", n)
        }
    }
}
