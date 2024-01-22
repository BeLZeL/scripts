fn add_function(x: i32, y: i32, res: &i32) -> &i32 {
    println!("The value of x + y is: {}", x + y);
    res = &(x + y);
    return res;
}

fn main() {
    let a=2;
    let b=3;
    let res2 = 0;
    let res1 = add_function(a, b, &res2);
    println!("Result from parameters is {}", res2);
    println!("Result from return is {}", res1);
}
