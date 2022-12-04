import time
from re import split as rsplit
import sys

def getBoundaries(part: str):
	return [int(x) for x in part.split("-")]

def findOverlaps(part1: str, part2: str) -> bool:
	bounds1 = getBoundaries(part1)
	bounds2 = getBoundaries(part2)
	if bounds1[0] == bounds2[0]:
		return True
	if bounds1[0] > bounds2[0]:
		return bounds1[1] <= bounds2[1]
	return bounds1[1] >= bounds2[1]

def findOverlaps_2(part1: str, part2: str) -> bool:
	bounds1 = getBoundaries(part1)
	bounds2 = getBoundaries(part2)
	if bounds1[0] > bounds2[0]:
		return bounds1[0] <= bounds2[1]
	return bounds1[1] >= bounds2[0]

def oneLiner(part2):
	with open("./input.txt") as file:
		overlaps = sum([int(pair[0]) == int(pair[2]) or (int(pair[0]) > int(pair[2]) and int(pair[1]) <= int(pair[3])) or (int(pair[0]) < int(pair[2]) and int(pair[1]) >= int(pair[3])) if not part2 else not(int(pair[1]) < int(pair[2]) or int(pair[0]) > int(pair[3])) for pair in [rsplit(r",|-", line.strip()) for line in file]])
		print(f"Total there are {overlaps} overlaps")


def main(input: str, part2 = False):
	with open(input) as file:
		overlaps = 0
		for line in file:
			if not part2:
				overlaps += int(findOverlaps(*line.split(",")))
			else:
				overlaps += int(findOverlaps_2(*line.split(",")))
		# print(f"Total there are {overlaps} overlaps")
		print(overlaps)

if __name__ == "__main__":
	input = sys.argv[1] if len(sys.argv) > 1 else "./input.txt"
	part = int(sys.argv[2]) if len(sys.argv) > 2 else 1
	main(input, part == 2)
	# print(f"Executed in {(time.perf_counter() - start) * 1000}ms")