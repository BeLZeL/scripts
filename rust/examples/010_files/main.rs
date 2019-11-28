use std::env;
use std::fs::File;
use std::io::Write;
use std::io::{BufReader, BufRead};

fn main() {

    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    
    if args.len() != 2 {
        println!("Specify a filename");
        return;
    }
    
    let filename = &args[1];
        
    let f = File::open(filename);

    match f {

        // File found, read the content
        Ok(file) => {
            println!("Found {:?}", file);        
            let buffered = BufReader::new(file);
            for line in buffered.lines() {
                println!("Read: {:?}", line);
            }        
        },
        
        // File not found, create and write one
        Err(error) => {
            println!("Error {}", error);
            
            let mut output = File::create(filename).unwrap();
            output.write_all(b"Hello, world!").unwrap();
        },

    };
}
