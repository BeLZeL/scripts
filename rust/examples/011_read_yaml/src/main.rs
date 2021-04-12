use std::fs::File;
use structopt::StructOpt;

#[derive(Debug, serde::Deserialize)]
pub struct Rules {
   #[serde(flatten)]
   pub global_conf: RateLimiterConf,
   pub service_limiters: Vec<RateLimiterDesc>,
}

#[derive(Debug, serde::Deserialize)]
pub struct RateLimiterDesc {
   pub name: String,
   #[serde(flatten)]
   pub conf: RateLimiterConf,
}

#[derive(Debug, serde::Deserialize)]
pub struct RateLimiterConf {
   pub lim_req_rate: u32,
   pub ban_duration_ms: u32,
}

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
   let f = File::open(&opts.file)?;
   let s = read_rules(&f)?;
   
   println!("Rules: {:#?}", s);

   println!("global_conf.lim_req_rate: {:?}", s.global_conf.lim_req_rate);

   for service in s.service_limiters.iter() {
      println!("name: {:?} : lim_req_rate {:?}", service.name, service.conf.lim_req_rate);
   }

   Ok(())
}

fn read_rules(file: &File) -> Result<Rules, serde_yaml::Error> {
   let r = serde_yaml::from_reader(file)?;
   Ok(r)
}
