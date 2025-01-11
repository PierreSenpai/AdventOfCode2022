from utils import filereader

input = filereader(10,True)

numberofcycles = 0
cycles = [20,60,100,140,180,220]
xchanges = [1]
sum_signal_strengths = 0


def check(n):
    if n+1 in cycles:
        cycles.remove(n+1)
        return xchanges
    return False

def sum_of_x(list):
    x = 0
    for change in list:
        x += int(change)
    return x

def signal_strength():
    list = check(numberofcycles)
    if list:
        valueofx = sum_of_x(list)
        signal_strength = valueofx * (numberofcycles+1)
        print(signal_strength)
        global sum_signal_strengths
        sum_signal_strengths += signal_strength

for line in input:
    signal_strength()
    if line == "noop":
        numberofcycles +=1
        signal_strength()
    else:
        increment = line.split()[1]
        numberofcycles += 1
        signal_strength()
        xchanges.append(increment)
        numberofcycles += 1

print(f"sum of all signal strengths: {sum_signal_strengths}")