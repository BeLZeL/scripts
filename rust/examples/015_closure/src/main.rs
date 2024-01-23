fn main() {

    // Hello World
    {
        let print_text = || println!("Defining Closure");
        print_text(); // show "Defining Closure"
    }

    // Inside
    {
        let add_one = |x: i32| println!("Sum {}", x + 1);
        add_one(2); // show "Sum 3"
    }

    // With Parameter
    {
        let add_one = |x: i32| x + 1;
        let result = add_one(2);
        println!("Result = {}", result); // show 3
    }

    // Multi-line
    {
        let squared_sum = |x: i32, y: i32| {
            let sum: i32 = x + y;
            let result: i32 = sum * sum;
            return result;
        };
        let result = squared_sum(5, 3); // (5+3)²
        println!("Result = {}", result); // show 64
    }

    // Capturing
    {
        let num = 100;
        let print_num = || println!("Number = {}", num);
        print_num(); // show 100
    }

    // Capturing with modification
    {
        let mut num = 100;
        let mut print_num = || { num = 12 ; println!("Number = {}", num); };
        print_num(); // show 12
        println!("Number = {}", num); // show 12
    }

    // Map
    {
        let numbers: Vec<i32> = vec![1, 2, 3];
        let res: Vec<i32> = numbers.iter().map(|i| i + 1).collect();
        println!("Results = {:?}", res); // show [2, 3, 4]
    }
}
