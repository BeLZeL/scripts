#------------------------------------------------------------------------------
# Basics

# https://doc.rust-lang.org/rust-by-example/flow_control/for.html
# 1, 2, 3, 4, 5
for y in 1..=5
# 1, 2, 3, 4
for y in 1..5

#------------------------------------------------------------------------------
# Convert


#------------------------------------------------------------------------------
# https://doc.rust-lang.org/std/string/struct.String.html
# Empty string
let mut chaine = String::new();
let mut chaine = String::from("");
let mut chaine = "".to_string();

# Concatene string
chaine += &"X".to_string();
