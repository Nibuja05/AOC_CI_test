use std::collections::HashMap;
use std::env;
use std::process;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    let config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });
    let hands = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
        ("A", 1),
        ("B", 2),
        ("C", 3),
    ]);
    task1(&config, &hands);
    task2(&config, &hands);
}

fn task2(config: &Config, hands: &HashMap<&str, i32>) {
    let mut total_score = 0;
    if let Ok(lines) = read_lines(config.file.clone()) {
        for line in lines {
            if let Ok(game) = line {
                let vec: Vec<&str> = game.split_whitespace().collect();
                if hands[vec[1]] == 1 {
                    // Loss
                    total_score += modulo(hands[vec[0]] - 2, 3) + 1 ;
                } else if hands[vec[1]] == 2 {
                    // Draw
                    total_score += hands[vec[0]] + 3;
                } else {
                    // Win
                    total_score += modulo(hands[vec[0]], 3) + 1 + 6;
                }
            }
        }
    }
    println!("{}", total_score);
}


fn task1(config: &Config, hands: &HashMap<&str, i32>) {
    let mut total_score = 0;
    if let Ok(lines) = read_lines(config.file.clone()) {
        for line in lines {
            if let Ok(game) = line {
                let vec: Vec<&str> = game.split_whitespace().collect();
                let res = hands[vec[1]] - hands[vec[0]];
                total_score += hands[vec[1]];
                // Cause this tard language has no modulo operator. Dafuck?
                if modulo(res, 3) == 1 {
                    total_score += 6;
                } else if res == 0 {
                    total_score += 3;
                }
            }
        }
    }
    println!("{}", total_score)
}

fn modulo(num: i32, div: i32) -> i32 {
    ((num % div) + div) % div
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

struct Config {
    // path: String,
    file: String,
}

impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() != 2 {
            return Err("Not enough arguments");
        }
        // let path = args[0].clone();
        let file = args[1].clone();

        Ok(Config{ file })
    }
}