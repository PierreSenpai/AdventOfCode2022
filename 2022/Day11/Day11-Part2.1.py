import math

from utils import filereader

input = filereader(11,False)


def monkey_data():
    filter1 = lambda x: x
    new_input = list(filter(filter1, input))

    items, operations, divisionby, truemonkeys, falsemonkeys = [], [], [], [], []
    n_monkeys = int(len(new_input)/6)
    global monkey_activity
    monkey_activity = [0 for i in range(n_monkeys)]
    item_number = 0
    global listofallitems
    listofallitems = list()
    for n in range(n_monkeys):
        # getting line and removing prefix
        line = new_input[n*6 + 1].lstrip("  Starting items: ")
        # splitting items
        line = line.split(", ")
        # converting all items into ints and add list of those to 'items'-list
        listofitems = list()
        for item in line:
            listofitems.append(f"item{item_number}")
            item_number += 1
            listofallitems.append(item)
        items.append(listofitems)

        line = new_input[n*6 + 2].lstrip("  Operation: new = old ")
        operations.append(line.split())

        divisionby.append(new_input[n*6 + 3].split()[-1])

        truemonkeys.append(new_input[n*6 + 4].split()[-1])

        falsemonkeys.append(new_input[n*6 + 5].split()[-1])

    global all_divisors
    all_divisors = [int(divisor) for divisor in divisionby]
    global modulocollection
    modulocollection = dict()

    for number,item in enumerate(listofallitems):
        modulocollection[f"item{number}"] = list()
        for divisor in all_divisors:
            modulo = int(item) % divisor
            modulocollection[f"item{number}"].append(modulo)

    # print(f"all items: {listofallitems}")
    # print(f"all divisors: {all_divisors}")
    # print(modulocollection)
    return list(zip(items, operations, divisionby, truemonkeys, falsemonkeys))

def inspection_and_check(currentitem, operation, divisor):
    # updating worry level according to operation
    operator, number = operation

    add = lambda num1: num1 + int(number)
    add_old = lambda num1: num1 + num1
    mul = lambda num1: num1 * int(number)
    mul_old = lambda num1: num1 * num1

    if number == "old":
        if operator == "+":
            modulocollection[currentitem] = list(map(add_old, modulocollection[currentitem]))
        else:
            modulocollection[currentitem] = list(map(mul_old, modulocollection[currentitem]))
    else:
        if operator == "+":
            modulocollection[currentitem] = list(map(add, modulocollection[currentitem]))
        else:
            modulocollection[currentitem] = list(map(mul, modulocollection[currentitem]))

    # checking if new worry level is divisable by divisor
    divisor_index = all_divisors.index(divisor)
    modulo = modulocollection[currentitem][divisor_index]
    moduloupdater()
    if modulo == 0:
        return True
    else:
        return False

def moduloupdater():
    for k,v in modulocollection.items():
        for index, modulo in enumerate(v):
            modulocollection[k][index] = modulo % all_divisors[index]
    # print("-------------------------------------------------------")
    # print(modulocollection)

def itemlister(data):
    itemlist = [monkey[0] for monkey in data]
    return itemlist

def round_procedure(data,rounds):
    for round in range(rounds):
        for i,monkey in enumerate(data):
            items, operation, divisionby, monkey_if_true, monkey_if_false = monkey
            for item in items.copy():
                trueorfalse = inspection_and_check(item, operation, int(divisionby))
                if trueorfalse:
                    data[int(monkey_if_true)][0].append(monkey[0].pop(0))
                else:
                    data[int(monkey_if_false)][0].append(monkey[0].pop(0))
                monkey_activity[i] += 1
    return data

def calculate_level(activitylist):
    biggest = max(activitylist)
    activitylist.remove(biggest)
    secondbiggest = max(activitylist)
    return biggest * secondbiggest

def main(number_of_rounds):
    monkey_activity = []
    round_procedure(monkey_data(), number_of_rounds)

main(20)
# print(modulocollection)
print(monkey_activity)
# print(calculate_level(monkey_activity))