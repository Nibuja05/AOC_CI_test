

useMap = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

def getWinner(a, b) -> int:
	if a == "A":
		if b == "Z":
			return 0
		if b == "Y":
			return 2
	if a == "B":
		if b == "X":
			return 0
		if b == "Z":
			return 2
	if a == "C":
		if b == "Y":
			return 0
		if b == "X":
			return 2
	return 1

# Nicht sehr effektiv, funktioniert aber :P
def mapSymbol(a, b):
	outcome = useMap[b] - 1
	for testB in ["X", "Y", "Z"]:
		winner = getWinner(a, testB)
		if winner == outcome:
			return testB
	return b	


def main(part2 = False):
	with open("./input.txt") as file:
		total = 0
		for line in file:
			a, b = line.replace("\n", "").split(" ")
			winner = getWinner(a, b)
			if part2:
				winner = useMap[b] - 1
				b = mapSymbol(a, b)
			winAmount = useMap[b] + winner * 3
			total += winAmount
		print(f"Total: {total}")


if __name__ == "__main__":
	main(True)