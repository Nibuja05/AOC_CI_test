def find_largest_calory_amount():
    leader = 0
    current = 0

    with open("input.txt") as in_file:
        for line in in_file:
            if line == '\n':
                if current > leader:
                    leader = current
                current = 0
                print('--------')
            else:
                current += int(line)
                print(line)

    return leader


if __name__ == '__main__':
    print(find_largest_calory_amount())
