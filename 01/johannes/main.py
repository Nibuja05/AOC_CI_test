#nur Aufgabenteil 2

with open('input') as f:
    lines = f.readlines()

scores = [0,0,0]
elf_score = 0
for line in lines:
    line = line.strip()
    if line == "":
        scores.append(elf_score)
        scores.sort()
        scores = scores[1:]
        elf_score = 0
        continue
    elf_score+=int(line)

scores.append(elf_score)
scores.sort()
scores = scores[1:]
print(sum(scores))
