fn add(mut x: u8, y: u8) -> u8 {
    x += y;
    x
}

fn add_ptr(x: &mut u8, y: u8) -> u8 {
    *x += y;
    *x
}

fn main() {

    let mut x = 42;

    let mut z = add(x, 15);
    println!("Result {} == {}!", add(x, 15), z); // show 57 == 57

    z = add_ptr(&mut x, 15);
    println!("Result {} == {}!", x, z); // show 57 == 57

    z += 1;
    println!("Result {} != {}!", x, z); // show 57 != 58

}
