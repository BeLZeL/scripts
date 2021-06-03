use std::env;
use tokio_postgres::{NoTls, Error};


struct SqlOrderRow {
    id: String,
    status: String
}


#[tokio::main] // By default, tokio_postgres uses the tokio crate as its runtime.
async fn main() -> Result<(), Error> {

    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    
    if args.len() != 4 {
        println!("Specify dbuser, dbhost and dbname");
        return Ok(());
    }

    let dbuser = &args[1];
    let dbhost = &args[2];
    let dbname = &args[3];
    
    // https://docs.rs/tokio-postgres/0.7.2/tokio_postgres/config/struct.Config.html
    //let connect_with_keys = format!("user={} host={} dbname={}", dbuser, dbhost, dbname);
    let connect_with_url = format!("postgresql://{}@{}/{}", dbuser, dbhost, dbname);

    // Connect to the database.
    let (client, connection) =
        tokio_postgres::connect(&connect_with_url, NoTls).await?;

    // The connection object performs the actual communication with the database,
    // so spawn it off to run on its own.
    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });
    
    //------------

    // Now we can execute a simple statement that just returns its parameter.
    let rows = client
        .query("SELECT $1::TEXT", &[&"hello world"])
        .await?;

    // And then check that we got back the same string we sent over.
    let value: &str = rows[0].get(0);
    assert_eq!(value, "hello world");
    
    //------------
    
    let rows = client
        .query("SELECT id, status FROM orders", &[])
        .await?;
        
    let order = SqlOrderRow {
        id: rows[0].get(0),
        status: rows[0].get(1)
    };
    println!("Found id {} with status {} ", order.id, order.status);

    Ok(())
}

