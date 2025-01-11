with open('Data - Day 6') as f:
    Datenstrom = f.readlines()[0]

AnzahlAnBuchstaben, Gefunden, Sequenz = 0, False, []

for i in range(3):
    Sequenz.append(Datenstrom[0])
    Datenstrom = Datenstrom[1:]
    AnzahlAnBuchstaben += 1

def DuplikateCheck(Liste):
    return len(Liste) != len(set(Liste))

while not Gefunden:
    Buchstabe = Datenstrom[0]
    Sequenz.append(Buchstabe)
    if DuplikateCheck(Sequenz):
        Sequenz.pop(0)
        Datenstrom = Datenstrom[1:]
        AnzahlAnBuchstaben += 1
        # print("Buchstabe doppelt")
    else:
        Datenstrom = Datenstrom[1:]
        AnzahlAnBuchstaben += 1
        Gefunden = True
        # print("!!!Sequenz gefunden!!!")

print(f"Für Signal verarbeitete Buchstaben: {AnzahlAnBuchstaben}\nSequenz: {Sequenz}")

#---------------------------------------------------------------------------------------

with open('Data - Day 6') as f:
    Datenstrom = f.readlines()[0]

AnzahlAnBuchstaben, Gefunden, Sequenz = 0, False, []

for i in range(13):
    Sequenz.append(Datenstrom[0])
    Datenstrom = Datenstrom[1:]
    AnzahlAnBuchstaben += 1

while not Gefunden:
    Buchstabe = Datenstrom[0]
    Sequenz.append(Buchstabe)
    if DuplikateCheck(Sequenz):
        Sequenz.pop(0)
        Datenstrom = Datenstrom[1:]
        AnzahlAnBuchstaben += 1
        # print("Buchstabe doppelt")
    else:
        Datenstrom = Datenstrom[1:]
        AnzahlAnBuchstaben += 1
        Gefunden = True
        # print("!!!Sequenz gefunden!!!")

print(f"Für Nachricht verarbeitete Buchstaben: {AnzahlAnBuchstaben}\nSequenz: {Sequenz}")

