use std::collections::{BinaryHeap};

struct Elf {
    calorie_sum: Calories,
}

type Calories = u32;

fn main() {
    let input = include_str!("input");
    let elves = elves_from_input(input);
    let top_elf_calorie_sum = elves.iter().map(|elf| elf.calorie_sum).max();
    print!("The top elf carries {:?} calories.\n", top_elf_calorie_sum.unwrap());

    let top_3_calories_sum = elves.iter()
        .map(|elf| elf.calorie_sum)
        .collect::<BinaryHeap<Calories>>().into_sorted_vec().into_iter().rev()
        .take(3)
        .sum::<Calories>();
    print!("The top three elves carry {:?} calories.\n", top_3_calories_sum);
}

fn elves_from_input(input: &str) -> Vec<Elf> {
    input
        .split("\n\n")
        .map(to_elf)
        .collect::<Vec<Elf>>()
}

fn to_elf(string: &str) -> Elf {
    Elf {
        calorie_sum: string.lines().map(to_calorie).sum()
    }
}

fn to_calorie(line: &str) -> Calories {
    line.parse::<Calories>().unwrap()
}
