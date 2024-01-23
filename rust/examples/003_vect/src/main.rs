fn main() {
    let mut v = vec![1, 2, 3];

    println!("First value = {}", v[0]); //show 1
    println!("Number of values = {}", v.len()); //show 3
    println!("Values = {:?}", v); //show [1, 2, 3]
    v.push(4);
    println!("Values = {:?}", v); //show [1, 2, 3, 4]
    v.remove(2);
    println!("Values = {:?}", v); //show [1, 2, 4]

    //-----------------

    // an array without data type
    let a = [5, 4, 3, 2, 1];
    println!("a = {:?}", a); // show [5, 4, 3, 2, 1]

    // an array with data type and size
    let b: [i32; 5] = [1, 2, 3, 4, 5];
    println!("b = {:?}", b); // show [1, 2, 3, 4, 5]

    // an array with default values
    let c = [3; 5];
    println!("c = {:?}", c); // show [3, 3, 3, 3, 3]

    let colors = ["red", "green", "blue"];
    println!("colors = {:?}", colors); // show ["red", "green", "blue"]

    //-----------------
    // slice

    let numbers = [1, 2, 3, 4, 5];
    let slice = &numbers[1..3];
    println!("array = {:?}", numbers); // show [1, 2, 3, 4, 5]
    println!("slice = {:?}", slice); // show [2, 3]

    //-----------------
    // mutable slice
    let mut colors = ["red", "green", "yellow", "white"];
    println!("array = {:?}", colors); // show ["red", "green", "yellow", "white"]
    let sliced_colors = &mut colors[1..3];
    println!("original slice = {:?}", sliced_colors); // show ["green", "yellow"]
    sliced_colors[1] = "purple";
    println!("changed slice = {:?}", sliced_colors); // show ["green", "purple"]
    colors[1] = "black"; // sliced_colors can't be used after
    println!("array = {:?}", colors); // show ["red", "black", "purple", "white"]

    // Iter
    {
        let numbers = vec![1, 2, 3];
        let mut numbers_iterator = numbers.iter();
        println!("{:?}, {:?}, {:?}, {:?}", numbers_iterator.next(), numbers_iterator.next(), numbers_iterator.next(), numbers_iterator.next()); // show Some(1), Some(2), Some(3), None
        numbers_iterator = numbers.iter();
        println!("{:?}, {:?}, {:?}", numbers_iterator.next().unwrap(), numbers_iterator.next().unwrap(), numbers_iterator.next().unwrap()); // show 1, 2, 3
        for number in numbers.iter() {
            println!("{}", number); // show 1 2 3
        }
    }

    // Iter_mut
    {
        let mut numbers = vec![1, 2, 3];
        for number in numbers.iter_mut() {
            *number = *number * 2;
            println!("{}", number); // show 2 4 6
        }
    }
}
