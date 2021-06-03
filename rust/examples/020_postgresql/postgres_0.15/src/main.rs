use std::env;
use postgres::{Connection, TlsMode};

struct SqlOrderRow {
    id: String,
    status: String
}

fn main() {  
    
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    
    if args.len() != 4 {
        println!("Specify dbuser, dbhost and dbname");
        return;
    }

    let dbuser = &args[1];
    let dbhost = &args[2];
    let dbname = &args[3];
    
    // https://docs.rs/tokio-postgres/0.7.2/tokio_postgres/config/struct.Config.html
    //let connect_with_keys = format!("user={} host={} dbname={}", dbuser, dbhost, dbname);
    let connect_with_url = format!("postgresql://{}@{}/{}", dbuser, dbhost, dbname);
    
    let conn = Connection::connect(connect_with_url, TlsMode::None)
            .unwrap();

    for row in &conn.query("SELECT id, status FROM orders", &[]).unwrap() {
        let order = SqlOrderRow {
            id: row.get(0),
            status: row.get(1)
        };
        println!("Found id {} with status {} ", order.id, order.status);
    }
}
