import os

def filereader(day,type):
    if type:
        with open(f'Input - Day {day}.txt') as f:
            return f.read().strip().split("\n")
    else:
        with open(f'Test - Day {day}.txt') as f:
            return f.read().strip().split("\n")


def daysetup(day):
    # create new directory
    os.mkdir(f"C:/Users/Pierre/Documents/.Programming/python/AdventOfCode2022/2022/Day{day}")
    # create both python files with filereader at the beginning
    lines = f"\
from utils import filereader\n\
\n\
input = filereader({day},False)\
"
    with open(f"2022/Day{day}/Day{day}-Part1.py","x") as f:
        f.write(lines)
    with open(f"2022/Day{day}/Day{day}-Part2.py", "x") as f:
        f.write(lines)
    # create both input files
    open(f"2022/Day{day}/Input - Day {day}.txt", "x")
    open(f"2022/Day{day}/Test - Day {day}.txt", "x")

if __name__ == "__main__":
    day = input("Number of Day: ")
    daysetup(day)
