// https://blog.rust-lang.org/2022/08/11/Rust-1.63.0.html#scoped-threads

use std::{thread, time};

fn main() {
    let mut a = vec![1, 2, 3];
    let mut x = 0;

    std::thread::scope(|s| {
        println!("Start main thread");
        s.spawn(|| {
            println!("Start first scoped thread");
            thread::sleep(time::Duration::from_millis(100));
            // We can borrow `a` here.
            dbg!(&a);
            println!("Finish first scoped thread");
        });
        s.spawn(|| {
            println!("Start second scoped thread");
            // We can even mutably borrow `x` here,
            // because no other threads are using it.
            x += a[0] + a[2];
            thread::sleep(time::Duration::from_millis(1000));
            println!("Finish second scoped thread");
        });
        println!("Finish main thread");
    });

    // After the scope, we can modify and access our variables again:
    println!("Check");
    a.push(4);
    assert_eq!(x, a.len());
}

// Start main thread
// Finish main thread
// Start first scoped thread
// Start second scoped thread
// [src/main.rs:16] &a = [
//     1,
//     2,
//     3,
// ]
// Finish first scoped thread
// Finish second scoped thread
// Check