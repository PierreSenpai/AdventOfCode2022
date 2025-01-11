import math

from utils import filereader

input = filereader(11,True)

def monkey_data():
    filter1 = lambda x: x
    new_input = list(filter(filter1, input))

    items, operations, divisionby, truemonkeys, falsemonkeys = [], [], [], [], []
    n_monkeys = int(len(new_input)/6)
    global monkey_activity
    monkey_activity = [0 for i in range(n_monkeys)]
    for n in range(n_monkeys):
        # getting line and removing prefix
        line = new_input[n*6 + 1].lstrip("  Starting items: ")
        # splitting items
        line = line.split(", ")
        # converting all items into ints and add list of those to 'items'-list
        listofitems = [int(n) for n in line]
        items.append(listofitems)

        line = new_input[n*6 + 2].lstrip("  Operation: new = old ")
        operations.append(line.split())

        divisionby.append(new_input[n*6 + 3].split()[-1])

        truemonkeys.append(new_input[n*6 + 4].split()[-1])

        falsemonkeys.append(new_input[n*6 + 5].split()[-1])

    return list(zip(items, operations, divisionby, truemonkeys, falsemonkeys))

def change_worry_level(worry_level, operation):
    operator, number = operation
    if number == "old":
        number = worry_level

    if operator == "+":
        worry_level += int(number)
    else:
        worry_level *= int(number)

    after_bored = math.floor(worry_level / 3)
    return after_bored

def monkeydecider(worry_level, divisor):
    if worry_level % int(divisor):
        return False
    else:
        return True

def itemlister(data):
    itemlist = [monkey[0] for monkey in data]
    return itemlist

def round_procedure(data,rounds):
    # print(itemlister(data))
    for round in range(rounds):
        for i,monkey in enumerate(data):
            items, operation, divisionby, monkey_if_true, monkey_if_false = monkey
            # print(f"monkey {i}:")
            for item in items.copy():
                new_worry_level = change_worry_level(item, operation)
                monkey_activity[i] += 1
                if monkeydecider(new_worry_level,divisionby):
                    monkey[0].pop(0)
                    data[int(monkey_if_true)][0].append(new_worry_level)
                else:
                    # print(type((data[int(monkey_if_false)][0])))
                    monkey[0].pop(0)
                    data[int(monkey_if_false)][0].append(new_worry_level)
        # print(itemlister(data))
    return data

def calculate_level(activitylist):
    biggest = max(activitylist)
    activitylist.remove(biggest)
    secondbiggest = max(activitylist)
    return biggest * secondbiggest

number_of_rounds = 20
monkey_activity = []
round_procedure(monkey_data(), number_of_rounds)

print(calculate_level(monkey_activity))



