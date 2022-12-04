from dataclasses import dataclass


@dataclass
class Elf:
    calories: int


def top_three_elves_calory_sum():
    top_3 = find_top_three_elves()
    calory_sum = 0
    for elf in top_3:
        calory_sum += elf.calories
    return calory_sum


def find_top_three_elves() -> list[Elf]:
    elves = get_elves_from_input()

    elves.sort(key=lambda elf: elf.calories, reverse=True)

    return elves[:3]


def get_elves_from_input() -> list[Elf]:
    elves: list[Elf] = []

    with open("input.txt") as in_file:
        current_elf = Elf(0)
        for line in in_file:
            if line == '\n':
                elves.append(current_elf)
                current_elf = Elf(0)
                print('--------')
            else:
                current_elf.calories += int(line)
                print(line)

    return elves


if __name__ == '__main__':
    print(top_three_elves_calory_sum())
