// https://docs.rs/tokio/latest/tokio/time/index.html

use std::time::Duration;
use tokio::time::sleep;

#[tokio::main]
async fn main() {
    println!("Start");
    sleep(Duration::from_millis(1000)).await;
    println!("1000 ms have elapsed");
}
