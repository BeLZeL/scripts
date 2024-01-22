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
    println!("{}", x);
    x = 3;
    println!("{}", x);
    /* ==================================================== */
    
    
    /* Pattern  ------------------------------------- */
    let y = if x == 1 { 3 } else { 5 };
    println!("y is {}", y); // 5
    /* ==================================================== */
    
    
    let mut z = 42;
    let w = &mut z;
    *w += 1;
    println!("{}", z); // 43
}
