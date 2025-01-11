with open('Data - Day 5') as f:
    Data = f.readlines()

Stapelung, AlleStapel = [],[]
for i in range(8):
    Stapelung.append(Data.pop(0).rstrip())
    j = 35 - len(Stapelung[-1])
    for k in range(j):
        l = Stapelung.pop() + " "
        Stapelung.append(l)
for i in range(9):
    Stapel = []
    Stelle = 1+4*i
    for j in range(8):
        Container = Stapelung[j][Stelle]
        if Container == " ":
            pass
        else:
            Stapel.append(Container)

    AlleStapel.append(Stapel)

Data.pop(0)
Data.pop(0)
# print(AlleStapel)

for i in Data:
    Anweisung = i.rstrip()
    Angaben = Anweisung.split(" ")
    Menge, Start, Ziel = int(Angaben[1]), int(Angaben[3]), int(Angaben[5])
    for j in range(Menge):
        # print(f"VON: Stapel {Start}: {AlleStapel[Start - 1]}, Stapel {Ziel}: {AlleStapel[Ziel-1]}")
        AktuellerContainer = AlleStapel[Start-1].pop(0)
        AlleStapel[Ziel-1].insert(0,AktuellerContainer)
        # print(f"ZU: Stapel {Start}: {AlleStapel[Start-1]}, Stapel {Ziel}: {AlleStapel[Ziel-1]}")

# print(AlleStapel)

obersteContainer = ""
for i in range(9):
    obersteContainer += AlleStapel[i][0]
print(f"obersten Container: {obersteContainer}")

#----------------------------------------------------------------------------------

with open('Data - Day 5') as f:
    Data = f.readlines()

Stapelung, AlleStapel = [],[]
for i in range(8):
    Stapelung.append(Data.pop(0).rstrip())
    j = 35 - len(Stapelung[-1])
    for k in range(j):
        l = Stapelung.pop() + " "
        Stapelung.append(l)
for i in range(9):
    Stapel = []
    Stelle = 1+4*i
    for j in range(8):
        Container = Stapelung[j][Stelle]
        if Container == " ":
            pass
        else:
            Stapel.append(Container)

    AlleStapel.append(Stapel)

Data.pop(0)
Data.pop(0)
# print(AlleStapel)

for i in Data:
    Anweisung = i.rstrip()
    Angaben = Anweisung.split(" ")
    Menge, Start, Ziel = int(Angaben[1]), int(Angaben[3]), int(Angaben[5])
    for j in range(Menge):
        # print(f"VON: Stapel {Start}: {AlleStapel[Start - 1]}, Stapel {Ziel}: {AlleStapel[Ziel-1]}")
        AktuellerContainer = AlleStapel[Start-1].pop(Menge-1-j)
        AlleStapel[Ziel-1].insert(0,AktuellerContainer)
        # print(f"ZU: Stapel {Start}: {AlleStapel[Start-1]}, Stapel {Ziel}: {AlleStapel[Ziel-1]}")

# print(AlleStapel)

obersteContainer = ""
for i in range(9):
    obersteContainer += AlleStapel[i][0]
print(f"obersten Container: {obersteContainer}")