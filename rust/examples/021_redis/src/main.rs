
use redis::Commands;

fn do_something() -> redis::RedisResult<()> {
    let client = redis::Client::open("redis://127.0.0.1:6379/")?;
    let mut con = client.get_connection()?;
    
    do_set(&mut con)?;
    do_set_hl(&mut con)?;
    do_commands_hl(&mut con)?;
    do_sub(&mut con)?;

    Ok(())
}

fn do_set(con: &mut redis::Connection) -> redis::RedisResult<()> {
    let _ : () = redis::cmd("SET").arg("my_key").arg(42).query(con)?;
    Ok(())
}

fn do_set_hl(con: &mut redis::Connection) -> redis::RedisResult<()> {
    let _ : () = con.set("my_counter", 666)?;
    Ok(())
}

fn do_commands_hl(con: &mut redis::Connection) -> redis::RedisResult<()> {
    let count : i32 = con.get("my_counter")?;
    println!("my_counter exists : {}", count);
    
    let count2 = con.get("my_counter2").unwrap_or(0i32);
    println!("my_counter doesn't exist : {}", count2);
    
    let k : Option<String> = con.get("missing_key")?;
    println!("Option String : {:?}", k);
    
    //let name : String = con.get("my_name")?;
    //let bin : Vec<u8> = con.get("my_binary")?;
    //let map : HashMap<String, i32> = con.hgetall("my_hash")?;
    //let keys : Vec<String> = con.hkeys("my_hash")?;
    //let mems : HashSet<i32> = con.smembers("my_set")?;
    //let (k1, k2) : (String, String) = con.get(&["k1", "k2"])?;

    Ok(())
}

fn do_sub(con: &mut redis::Connection) -> redis::RedisResult<()> {

    println!("You can try :\nPUBLISH channel_1 Hello\nPUBLISH channel_2 World\n");
    let mut pubsub = con.as_pubsub();
    pubsub.subscribe("channel_1")?;
    pubsub.subscribe("channel_2")?;

    loop {
        let msg = pubsub.get_message()?;
        let payload : String = msg.get_payload()?;
        println!("channel '{}': {}", msg.get_channel_name(), payload);
    }
}

fn main() -> redis::RedisResult<()> {
    do_something()?;
    Ok(())
}

