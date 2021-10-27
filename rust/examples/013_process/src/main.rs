use std::process::Command;
use std::io::{self, Write};

fn main() {
    let output = Command::new("/bin/cat")
                        .arg("Cargo.toml")
                        .output()
                        .expect("failed to execute process");

    println!("status: {}", output.status);
    println!("result: {:?}", output.stdout);
    io::stdout().write_all(&output.stdout).unwrap();
    io::stderr().write_all(&output.stderr).unwrap();

    assert!(output.status.success());
}
