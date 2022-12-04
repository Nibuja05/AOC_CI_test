use std::{
    fs::File,
    io::{BufRead, BufReader},
};

// fn calculate_game_score<S: AsRef<str>>(line: S) -> usize {
//     let line = line.as_ref();
//     match line {
//         "A X" => 1 + 3, // Rock    -- Rock
//         "B X" => 1 + 0, // Paper   -> Rock
//         "C X" => 1 + 6, // Scissor <- Rock
//         "A Y" => 2 + 6,
//         "B Y" => 2 + 3,
//         "C Y" => 2 + 0,
//         "A Z" => 3 + 0,
//         "B Z" => 3 + 6,
//         "C Z" => 3 + 3,
//         _ => unreachable!(),
//     }
// }

fn calculate_game_score<S: AsRef<str>>(line: S) -> usize {
    let line = line.as_ref();
    match line {
        // Rock -> 1
        // Paper -> 2
        // Scissor -> 3
        "A X" => 3 + 0,
        "B X" => 1 + 0,
        "C X" => 2 + 0,
        "A Y" => 1 + 3,
        "B Y" => 2 + 3,
        "C Y" => 3 + 3,
        "A Z" => 2 + 6,
        "B Z" => 3 + 6,
        "C Z" => 1 + 6,
        _ => unreachable!(),
    }
}

fn main() {
    let file = ::std::env::args()
        .skip(1)
        .next()
        .unwrap_or_else(|| String::from("./input"));
    let file = BufReader::new(File::open(file).expect("Input file not found"));
    let sum: usize = file
        .lines()
        .map(Result::unwrap)
        .map(calculate_game_score)
        .sum();
    println!("Total score: {sum}");
}
