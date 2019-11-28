//=============================================================================
trait ArmyUnit {

    fn get_name(&self) -> String {
        String::from("No Name")
    }

    fn calculate_price(&self) -> i32;
}
//-----------------------------------------------------------------------------
fn print_unit<T: ArmyUnit>(unit: T) {
    println!("Name : {} , Price : {}", unit.get_name(), unit.calculate_price())
}
//=============================================================================





//=============================================================================
struct FairyUnit {
    name: String,
    life: i32,
    attack: i32,
    fly: bool,
}
//-----------------------------------------------------------------------------
impl ArmyUnit for FairyUnit {

    fn calculate_price(&self) -> i32 {
        if self.fly {
            self.life * self.attack + 20
        } else {
            self.life * self.attack
        }
    }

    fn get_name(&self) -> String {
        self.name.clone()
    }
}
//=============================================================================





//=============================================================================
struct OrkUnit {
    name: String,
    life: i32,
    attack: i32,
}
//-----------------------------------------------------------------------------
impl ArmyUnit for OrkUnit {

    fn calculate_price(&self) -> i32 {
        self.life * self.attack + 3
    }
    
    fn get_name(&self) -> String {
        self.name.clone()
    }
}
//=============================================================================





//=============================================================================   
fn main() {
    let fairy_one = FairyUnit { name: String::from("Purple Fairy"), life: 3, attack:1, fly:true};
    let ork_one = OrkUnit { name: String::from("Big Ork"), life:8, attack:3};
    print_unit(fairy_one);
    print_unit(ork_one);
}
//=============================================================================   
