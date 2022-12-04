import sys

def top(vList: list, top):
	tops = []
	for _ in range(top):
		most = max(vList)
		tops.append(most)
		vList.remove(most)
	return tops


def main(path, part2 = False):
	elfList = []
	curSum = 0
	with open(path) as file:
		for line in file:
			if line.strip() == "":
				elfList.append(curSum)
				curSum = 0
				continue
			curSum += int(line)
	elfList.append(curSum)
	tops = top(elfList, 3) if part2 else top(elfList, 1)
	together = sum(tops)
	print(together)
	# print("Test most calories carried by an elf are: ", tops, together)


if __name__ == "__main__":
	input = sys.argv[1] if len(sys.argv) > 1 else "./input.txt"
	part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
	main(input, part == 2)