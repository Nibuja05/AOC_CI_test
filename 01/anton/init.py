
def top(vList: list, top):
	tops = []
	for _ in range(top):
		most = max(vList)
		tops.append(most)
		vList.remove(most)
	return tops


def main():
	elfList = []
	curSum = 0
	with open("./input.txt") as file:
		for line in file:
			if line.strip() == "":
				elfList.append(curSum)
				curSum = 0
				continue
			curSum += int(line)
	elfList.append(curSum)
	tops = top(elfList, 3)
	together = sum(tops)
	print("Test most calories carried by an elf are: ", tops, together)


if __name__ == "__main__":
	main()