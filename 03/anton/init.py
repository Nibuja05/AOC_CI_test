import time
from multiprocessing import Pool

def getPriority(item):
	return id - 96 if (id := ord(item)) > 90 else id - 38

def intersect(listA: list, listB: list) -> list:
	return list(filter(lambda x: x in listB, listA))

def firstIntersect(listA: list, listB: list):
	for x in listA:
		if x in listB:
			return x

def getCommonItemPriority(itemList: str):
	half = int(len(itemList)/2)
	commons = list(set(itemList[:half]).intersection(itemList[half:]))
	if len(commons) > 0:
		return getPriority(commons[0])
	return 0

def getCommonBadgePriority(rucksacks):
	commons = list(set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2]))
	if len(commons) > 0:
		return getPriority(commons[0])
	return 0

def main(part2 = False):
	with open("./gen_input.txt") as file:
		priorities = 0
		for line in file:
			if not part2:
				priorities += getCommonItemPriority(line)
			else:
				rucksacks = [line[:-1], next(file, "")[:-1], next(file, "")[:-1]]
				priorities += getCommonBadgePriority(rucksacks)
		print(f"Total priority of all inventories is {priorities}")


def itemReader(file):
	for line in file:
		yield [line[:-1], next(file, "")[:-1], next(file, "")[:-1]]

def main_multi():
	with open("./gen_input.txt") as file:
		with Pool() as pool:
			result = pool.map(getCommonBadgePriority, itemReader(file))
			print(f"Total priority of all inventories is {sum(result)}")


if __name__ == "__main__":
	start = time.perf_counter()
	# main(False)
	# main(True)
	main_multi()
	print(f"Executed in {(time.perf_counter() - start) * 1000}ms")