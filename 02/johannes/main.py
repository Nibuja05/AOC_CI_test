#read input 
import os
importfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"input")
with open(importfile) as f:
    lines = f.readlines()


score = 0
score2 = 0
for line in lines:
    line = line.strip()
    line = line.split(" ")
    opponent = line[0]
    me = line[1]
    if me == "X":
        score += 1
        if opponent == "A":
            score += 3
        if opponent == "B":
            pass
        if opponent == "C":
            score += 6
    if me == "Y":
        score += 2
        if opponent == "A":
            score +=6
        if opponent == "B":
            score += 3
        if opponent == "C":
            pass
    if me == "Z":
        score += 3
        if opponent == "A":
            pass          
        if opponent == "B":
            score +=6 
        if opponent == "C":
            score += 3

    if opponent == "A":
        if me == "X":
            pass
            score2 += 3
        if me == "Y":
            score2 += 3
            score2 += 1
        if me == "Z":
            score2 += 6
            score2 += 2
    if opponent == "B":
        if me == "X":
            pass
            score2 += 1
        if me == "Y":
            score2 += 3
            score2 += 2
        if me == "Z":
            score2 += 6
            score2 += 3
    if opponent == "C":
        if me == "X":
            pass
            score2 += 2
        if me == "Y":
            score2 += 3
            score2 += 3
        if me == "Z":
            score2 += 6
            score2 += 1


print(score)
print(score2)
