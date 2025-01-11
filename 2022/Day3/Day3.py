import string

with open('Data - Day 3') as f:
    rucksacks = f.readlines()

priorities = list(string.ascii_letters)
priorities_sum = 0

for i in rucksacks:
    rucksack = i[:-1]
    length = len(rucksack)
    cut = int(length/2)
    compartment1 = rucksack[:cut]
    compartment2 = rucksack[cut:]
    for i in range(1,53):
        if priorities[i-1] in compartment1 and priorities[i-1] in compartment2:
            priorities_sum += i
        else:
            continue
print(f"sum of the priorities: {priorities_sum}")
# --------------------------------------------------------------------------------

priorities_sum = 0

while rucksacks:
    group = []
    for i in rucksacks[:3]:
        group.append(i)
    for j in range(1,53):
        badge = priorities[j-1]
        if badge in group[0] and badge in group[1] and badge in group[2]:
            priorities_sum += j
        else:
            continue
    for i in range(3):
        rucksacks.pop(0)


print(f"sum of the badge-priorities: {priorities_sum}")

