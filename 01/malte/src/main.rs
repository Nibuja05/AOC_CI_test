//! Find the elves carrying the most calories.
use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn either_calories_or_blank<S: AsRef<str>>(inp: S) -> Option<usize> {
    inp.as_ref().parse().ok()
}

#[derive(Default)]
struct TopThree {
    first: usize,
    second: usize,
    third: usize,
}

#[derive(Default)]
struct TopCal {
    top: TopThree,
    curr_sum: usize,
}

impl TopCal {
    const fn push_line(self, line: Option<usize>) -> Self {
        match line {
            Some(cal) => TopCal {
                curr_sum: self.curr_sum + cal,
                ..self
            },
            None => TopCal {
                curr_sum: 0,
                top: TopThree::push_sum(self.top, self.curr_sum),
            },
        }
    }
}

impl TopThree {
    const fn push_sum(self, sum: usize) -> Self {
        let (first, second, third) = if sum > self.first {
            (sum, self.first, self.second)
        } else if sum > self.second {
            (self.first, sum, self.second)
        } else if sum > self.third {
            (self.first, self.second, sum)
        } else {
            (self.first, self.second, self.third)
        };
        Self {
            first,
            second,
            third,
        }
    }
    const fn total_sum(&self) -> usize {
        self.first + self.second + self.third
    }
}

fn main() {
    let file = ::std::env::args()
        .skip(1)
        .next()
        .unwrap_or_else(|| String::from("./input"));
    let file = BufReader::new(File::open(file).expect("Input file not found"));
    let TopCal { top, .. } = file
        .lines()
        .map(Result::unwrap)
        .map(either_calories_or_blank)
        .collect();
    println!("{}", top.total_sum());
}

impl FromIterator<Option<usize>> for TopCal {
    fn from_iter<T: IntoIterator<Item = Option<usize>>>(iter: T) -> Self {
        let max = iter.into_iter().fold(Self::default(), TopCal::push_line);
        // Make sure to read one extra empty line at the end
        TopCal::push_line(max, None)
    }
}
