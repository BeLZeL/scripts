//-------------------------------------
// $ ./target/debug/opt_args 
// error: The following required arguments were not provided:
//     --file <file>
// 
// USAGE:
//     opt_args --file <file>
// 
// For more information try --help
//-------------------------------------
// ./target/debug/opt_args --help
//     Finished dev [unoptimized + debuginfo] target(s) in 0.01s
// opt_args 0.1.0
// 
// USAGE:
//     opt_args --file <file>
// 
// FLAGS:
//     -h, --help       Prints help information
//     -V, --version    Prints version information
// 
// OPTIONS:
//     -f, --file <file> 
//-------------------------------------

use structopt::StructOpt;

#[derive(Debug, StructOpt)]
struct Opt {
   #[structopt(short, long)]
   file: String,
}

fn main() {
   let opts = Opt::from_args();
   if let Err(e) = checked_main(&opts) {
       eprintln!("Got error: {:?}", e);
   }
}

fn checked_main(opts: &Opt) -> Result<(), Box<dyn std::error::Error>> {
   
   println!("File: {:#?}", &opts.file);

   Ok(())
}
