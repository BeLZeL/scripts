fn main() {

    /*=====================================================
    * error[E0384]: cannot assign twice to immutable variable `x`
    
    let x = 2;
    println!("{}", x);
    x = 3;
    println!("{}", x);
    */

    /* Solution : mut ------------------------------------- */
    let mut x = 2;
    println!("{}", x); // show 2
    x = 3;
    println!("{}", x); // show 3
    /* ==================================================== */


    /* Pattern -------------------------------------------- */
    let y = if x == 1 { 3 } else { 5 };
    println!("y is {}", y); // show 5
    /* ==================================================== */


    /* Mut et pointeur ------------------------------------ */
    let mut z = 42;
    let w = &mut z;
    *w += 1;
    println!("{}", z); // show 43
    /* ==================================================== */


    /* if let --------------------------------------------- */
    if let Ok(x) = "123".parse::<i32>() {
        println!("double that and you get {}!", x * 2); // show 246
    }
    /* ==================================================== */


    /* frozen var --------------------------------------------- */
    let mut age = 100;
    {
        // shadowing by immutable age variable
        let age = age;
        // age = 2; // error, age variable is frozen in this scope
        println!("age variable inner block = {}", age); // show 100
        // age goes out of scope
    }
    // age variable is not frozen in this scope
    age = 3;
    println!("age variable outer block = {}", age); // show 3
    /* ==================================================== */
}
