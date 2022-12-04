import sys
from random import randint, random

HELP = """Generates an input file with a specific size for day 3. Possible arguments:
- line Count [OPTIONAL], default: 1200
- max line length [OPTIONAL], default: 50
- min line length [OPTIONAL], default: 10

Output file name: "gen_input.txt"
"""

allChars = [chr(x + 65 + (6 if x > 26 else 0)) for x in range(0, 26*2)]

def randomChar(exclude: list[str] = []) -> str:
	possibleChars = excludeList(allChars, exclude)
	return possibleChars[randint(0, len(possibleChars)) - 1]

def excludeList(itemList: list[str], exclude: list[str]) -> list[str]:
	return list(filter(lambda x: x not in exclude, itemList))

def getCharList(exclude: list[str], length: int) -> list[str]:
	newList = []
	for _ in range(length):
		newList.append(randomChar(exclude + newList))
	return newList

def pickRandomly(charList: list[str], length: int) -> str:
	return [charList[randint(0, len(charList) - 1)] for _ in range(length)]

def main(args):
	if len(args) > 0 and args[0] == "-h":
		print(HELP)
		sys.exit()

	lineCount = int(args[0]) if len(args) > 0 else 1200
	maxLen = int(args[1]) if len(args) > 1 else 50
	minLen = int(args[2]) if len(args) > 2 else 10

	outputFile = "./gen_input.txt"

	with open(outputFile, "a") as file:
		file.seek(0)
		file.truncate()
		for x in range(0, lineCount):
			if x % 3 == 0:
				blockItem = randomChar()
				blockExcludes = [blockItem]
			commonItem = randomChar(blockExcludes)
			blockExcludes.append(commonItem)
			hLength = int(random() * (maxLen / 2) + (minLen / 2))
			length = hLength * 2

			firstChars = getCharList(blockExcludes, 6)
			line = pickRandomly(firstChars, hLength)
			blockExcludes += firstChars

			secondChars = getCharList(blockExcludes, 6)
			line += pickRandomly(secondChars, hLength)
			blockExcludes += secondChars

			line[randint(0, hLength - 1)] = commonItem
			line[randint(hLength, length - 1)] = commonItem
			while True:
				if line[(blockIndex := randint(0, length - 1))] == commonItem:
					continue
				line[blockIndex] = blockItem
				break
			file.write("".join(line) + ("\n" if x < lineCount - 1 else ""))


if __name__ == "__main__":
	main(sys.argv[1:])