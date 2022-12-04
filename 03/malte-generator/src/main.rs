//! Some restrictions
//! - Number of lines needs to be divisible by three
//! - Number of chars per line need to be divisible by three
//! - Every line can be split in two halves sharing exactly one character
//! - Case matters
//! - The file can be split into groups of three lines. These three lines share exactly one character
use clap::Parser;
use lazy_static::lazy_static;
use rand::{
    rngs::SmallRng,
    seq::{IteratorRandom, SliceRandom},
    Rng, SeedableRng,
};

use std::{
    fs::File,
    io::{BufWriter, Write},
    ops::Range,
    path::PathBuf,
};

lazy_static! {
    static ref CHARS: Vec<char> = ('a'..'z').chain('A'..'Z').collect();
    static ref ARGS: Args = Args::parse();
}

#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(short = 'n', long, default_value = "20000")]
    elf_groups: usize,
    #[arg(short = 'i', long, default_value = "60")]
    min_line: usize,
    #[arg(short = 'x', long, default_value = "2000")]
    max_line: usize,
    #[arg(short, long)]
    out_file: PathBuf,
}

impl Args {
    pub fn half_line_range(&self) -> Range<usize> {
        (self.min_line / 2)..(self.max_line / 2)
    }
}

fn replace_rand<I>(rng: &mut rand::rngs::SmallRng, list: &mut Vec<I>, item: I) {
    debug_assert!(list.len() > 0);
    let idx = rng.gen_range(0..list.len());
    list[idx] = item;
}

fn gen_triple(rng: &mut rand::rngs::SmallRng) -> [String; 3] {
    let amounts = ARGS.half_line_range().choose_multiple(rng, 3);
    // The badge that is shared in this triple
    let badge: char = *CHARS.choose(rng).unwrap();
    let mut lines: Vec<String> = amounts
        .iter()
        .map(|&amount| {
            debug_assert!(amount > 0);
            // The item that is shared between the halves
            let wrong_between_halves: char = *CHARS
                .iter()
                .filter(|&&char| char != badge)
                .choose(rng)
                .unwrap();
            let possible_left = CHARS
                .iter()
                .filter(|&&char| char != wrong_between_halves)
                .filter(|&&char| char != badge)
                .copied()
                .choose_multiple(rng, CHARS.len() / 2 - 1);
            let possible_right: Vec<_> = CHARS
                .iter()
                .filter(|&char| !possible_left.contains(char))
                .copied()
                .collect();
            let mut left: Vec<_> = (0..amount)
                .map(|_| rng.gen_range(0..possible_left.len()))
                .map(|idx| possible_left[idx])
                .collect();
            let mut right: Vec<_> = (0..amount)
                .map(|_| rng.gen_range(0..possible_right.len()))
                .map(|idx| possible_right[idx])
                .collect();
            debug_assert!(left.len() == amount);
            debug_assert!(right.len() == amount);
            // Insert the badge
            replace_rand(
                rng,
                if rand::random() {
                    &mut left
                } else {
                    &mut right
                },
                badge,
            );
            // Insert the wrong items
            replace_rand(rng, &mut left, wrong_between_halves);
            replace_rand(rng, &mut right, wrong_between_halves);
            debug_assert!(left.len() == right.len());
            debug_assert!(left.len() == amount);
            debug_assert!(right.len() == amount);
            left.into_iter().chain(right).collect::<String>()
        })
        .collect();
    debug_assert!(lines.len() == 3);
    let third = lines.pop().unwrap();
    let second = lines.pop().unwrap();
    let first = lines.pop().unwrap();
    [first, second, third]
}

fn main() {
    let mut outfile = BufWriter::new(File::create(&ARGS.out_file).expect("Can write outfile"));
    let mut rng = SmallRng::from_rng(rand::thread_rng()).expect("Init rng");
    (0..ARGS.elf_groups)
        .flat_map(|_| gen_triple(&mut rng))
        .inspect(|line| debug_assert!(line.len() % 2 == 0))
        .for_each(|line| writeln!(outfile, "{line}").expect("Writing works"));
    outfile.flush().expect("Flushing works");
}
