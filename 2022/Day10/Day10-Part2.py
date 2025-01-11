from utils import filereader

input = filereader(10,True)

sprite = [0,1,2]
row_length = 40
numberofrows = 6

spritecopy = sprite.copy()
for row in range(1, 6):
    for i,v in enumerate(spritecopy):
        sprite.append(row*row_length+v)

crt = 0

numberofcycles = 0

display = {}

def changesprite(increment):
    for i,v in enumerate(sprite):
        sprite[i] += increment

def paint():
    if crt in sprite:
        display[crt] = "#"
    else:
        display[crt] = "."

while numberofcycles < 241:
    try:
        line = input[0]
    except IndexError:
        pass
    if line == "noop":
        paint()
        numberofcycles +=1
        crt += 1
        try:
            input.pop(0)
        except IndexError:
            pass
    else:
        increment = int(line.split()[1])
        paint()
        numberofcycles += 1
        crt += 1
        paint()
        changesprite(increment)
        numberofcycles += 1
        crt += 1
        try:
            input.pop(0)
        except IndexError:
            pass

for row in range(1,numberofrows+1):
    for pixel in range((row-1) * row_length, row * row_length):
        print(display[pixel], end="")
    print("")