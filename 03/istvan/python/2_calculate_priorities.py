from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class ElfGroup:
    elf_1: str
    elf_2: str
    elf_3: str


def in_groups_of_3(lines: Iterator[str]) -> Iterator[List[str]]:
    partial_line_group = []
    for line in lines:
        partial_line_group.append(line)
        if len(partial_line_group) == 3:
            yield partial_line_group
            partial_line_group = []


def input_to_elf_groups() -> Iterator[ElfGroup]:
    with open("input") as in_file:
        line_groups = in_groups_of_3(in_file.readlines())
        for line_group in line_groups:
            yield line_group_to_elf_group(line_group)


def line_group_to_elf_group(line_group: Iterator[str]):
    lines = [line.strip() for line in line_group]
    elf_group = ElfGroup(
        elf_1=lines[0],
        elf_2=lines[1],
        elf_3=lines[2],
    )
    print(elf_group)
    return elf_group


def find_common_item(elf_group: ElfGroup) -> str:
    for char_a in elf_group.elf_1:
        for char_b in elf_group.elf_2:
            if char_a == char_b:
                for char_c in elf_group.elf_3:
                    if char_c == char_b:
                        return char_c


def item_to_priority(item: str):
    char_ord = ord(item)
    # lowercase
    if char_ord > 96:
        return char_ord - 96
    # uppercase
    else:
        return char_ord - 64 + 26


def main():
    elf_groups = [group for group in input_to_elf_groups()]
    common_items = [find_common_item(group) for group in elf_groups]
    priority_values = [item_to_priority(item) for item in common_items]
    priority_sum = sum(priority_values)
    print(priority_sum)

    # solution
    assert priority_sum == 2415


if __name__ == '__main__':
    main()
