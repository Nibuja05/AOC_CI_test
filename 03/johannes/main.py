#read input 
import time
begin = time.time()
import os
importfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"input")
with open(importfile) as f:
    lines = f.readlines()

score1 =0
score2 =0

for line in lines:
    line = line.strip()
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    compartment1 = set(compartment1)
    compartment2 = set(compartment2)
    letter = compartment1 & compartment2
    letter=letter.pop()
    if letter.islower():
        priority = ord(letter) - ord("a") + 1
    else:
        priority = ord(letter) - ord("A") + 27
    score1 += priority



tripels = [ [lines[0+x],lines[1+x],lines[2+x]] for x in range(0,len(lines),3)]

for tripel in tripels:
    rucksack1 = set(tripel[0].strip())
    rucksack2 = set(tripel[1].strip())
    rucksack3 = set(tripel[2].strip())

    

    letter = rucksack1 & rucksack2 & rucksack3
    letter=letter.pop()
    if letter.islower():
        priority = ord(letter) - ord("a") + 1
    else:
        priority = ord(letter) - ord("A") + 27
    score2 += priority

print(score1)
print(score2)
end = time.time()
print(end-begin)