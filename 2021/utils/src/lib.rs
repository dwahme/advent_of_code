use std::env;
use std::fs;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


pub fn get_input(filename: &str) -> String {
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    contents
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn get_input_lines<P>(filename: &str) -> Vec<String> {
    let mut out = Vec::new();

    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines(filename) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                out.push(ip)
            }
        }
    }

    out
}

pub fn get_input_lines_int(filename: &str) -> Vec<i32> {
    let mut out = Vec::new();

    let lines = get_input_lines::<i32>(filename);

    for line in lines
    {
        out.push(line.parse::<i32>().unwrap())
    }

    out
}
