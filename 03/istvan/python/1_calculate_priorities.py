from dataclasses import dataclass
from typing import Iterator


@dataclass
class Rucksack:
    compartment_1: str
    compartment_2: str


def input_to_rucksacks() -> Iterator[Rucksack]:
    with open("input") as in_file:
        for line in in_file:
            stripped = line.strip('\n')
            yield Rucksack(
                compartment_1=stripped[:int(len(stripped) / 2)],
                compartment_2=stripped[int(len(stripped) / 2):],
            )


def find_error(rucksack: Rucksack) -> str:
    for char_a in rucksack.compartment_1:
        for char_b in rucksack.compartment_2:
            if char_a == char_b:
                return char_a


def item_to_priority(item: str):
    char_ord = ord(item)
    # lowercase
    if char_ord > 96:
        return char_ord - 96
    # uppercase
    else:
        return char_ord - 64 + 26


def main():
    rucksacks = input_to_rucksacks()
    erroneous_items = [find_error(rucksack) for rucksack in rucksacks]
    priorities = [item_to_priority(item) for item in erroneous_items]
    print(sum(priorities))


if __name__ == '__main__':
    main()
