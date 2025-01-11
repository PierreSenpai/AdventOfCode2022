with open('Data - Day 1') as f:
    lines = f.readlines()

elfen = lines.count("\n")+1

alleelfen = []
print("Elfen:",elfen)
try:
    for i in range(elfen):
        trennung = lines.index("\n")
        kalorien = 0
        for j in lines[0:trennung]:
            kalorien += int(j)
        alleelfen.append(kalorien)
        for k in range(trennung+1):
            del lines[0]


except:
    kalorien = 0
    for l in lines:
        kalorien += int(l)
    alleelfen.append(kalorien)

print("Kalorien:",alleelfen)

biggest = 0
for i in alleelfen:
    if biggest < i:
        biggest = i
    else:
        pass
elf1 = biggest
alleelfen.remove(biggest)
biggest = 0

for i in alleelfen:
    if biggest < i:
        biggest = i
    else:
        pass
elf2 = biggest
alleelfen.remove(biggest)
biggest = 0

for i in alleelfen:
    if biggest < i:
        biggest = i
    else:
        pass
elf3 = biggest

top3 = elf1 + elf2+ elf3

print("1.Elf:",elf1,"2.Elf:",elf2,"3.Elf:",elf3)

print("Top 3:",top3)