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
    println!("Folder {}", config.path);
    println!("File {}", config.file);
    task1(&config);
    task2(&config);
}

fn task1(config: &Config){
    let mut elf = Elf{id: 0, calories: 0};
    if let Ok(lines) = read_lines(config.file.clone()) {
        let mut calories = 0;
        let mut current_elf = 0;
        for line in lines {
            if let Ok(calory) = line {
                if calory == "" {
                    if calories > elf.calories {
                        elf.calories = calories;
                        elf.id = current_elf;
                    }
                    calories = 0;
                    current_elf += 1;
                } else {
                    calories += calory.parse::<u32>().unwrap();
                }
            }
        }
        if calories > elf.calories {
            elf.calories = calories;
            elf.id = current_elf;
        }
    }
    println!("{}: {}", elf.id, elf.calories);
}

fn task2(config: &Config){
    let mut absolute_calories = [0, 0, 0];
    if let Ok(lines) = read_lines(config.file.clone()) {
        let mut calories = 0;
        for line in lines {
            if let Ok(calory) = line {
                if calory == "" {
                    let mut found = false;
                    for item in absolute_calories.iter_mut() {
                        if item < &mut calories {
                            *item = calories;
                            found = true;
                            break;
                        }
                    }
                    if found {
                        absolute_calories.sort();
                    }
                    calories = 0;
                } else {
                    calories += calory.parse::<u32>().unwrap();
                }
            }
        }
        
        for item in absolute_calories.iter_mut() {
            if item < &mut calories {
                *item = calories;
                break;
            }
        }
    }

    println!("{} - {} - {}", absolute_calories[0], absolute_calories[1], absolute_calories[2]);
    println!("Sum: {}", absolute_calories.iter().sum::<u32>());
}

struct Elf {
    id: u16,
    calories: u32,
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

struct Config {
    path: String,
    file: String,
}

impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() != 2 {
            return Err("Not enough arguments");
        }
        let path = args[0].clone();
        let file = args[1].clone();

        Ok(Config{ path, file })
    }
}