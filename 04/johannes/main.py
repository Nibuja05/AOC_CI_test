import itertools
import os
importfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"input")
with open(importfile) as f:
    lines = f.readlines()

score1 =0
score2 =0

for line in lines:
    line = line.strip()
    line = line.split(",")
    first = line[0].split("-")
    second = line[1].split("-")
    firstlow = int(first[0])
    firsthigh = int(first[1])
    secondlow = int(second[0])
    secondhigh = int(second[1])
    if firstlow<=secondlow and firsthigh>=secondhigh:
        score1+=1
    elif firstlow>=secondlow and firsthigh<=secondhigh:
        score1+=1
    for x,y in itertools.product(range(firstlow,firsthigh+1),range(secondlow,secondhigh+1)):
        if x == y:
            score2+=1
            break   
print(score1)
print(score2)
