with open('Data - Day 2') as f:
    alleZüge = f.readlines()

Punktzahl1, Punktzahl2, AnzahlStein, AnzahlPapier, AnzahlSchere, Siege, Unentschieden, Niederlagen = 0,0,0,0,0,0,0,0
Stein = ["A","X"]
Papier = ["B", "Y"]
Schere = ["C","Z"]

for i in alleZüge:
    if i[2] in Stein:
        Punktzahl1 += 1
        AnzahlStein += 1
        if i[0] in Schere:
            Punktzahl2 += 6
            Siege += 1
        elif i[0] in Stein:
            Punktzahl2 += 3
            Unentschieden += 1
        else: #Papier
            Niederlagen += 1
    elif i[2] in Papier:
        Punktzahl1 += 2
        AnzahlPapier += 1
        if i[0] in Stein:
            Punktzahl2 += 6
            Siege += 1
        elif i[0] in Papier:
            Punktzahl2 += 3
            Unentschieden += 1
        else: #Schere
            Niederlagen += 1
    else: #Schere
        Punktzahl1 += 3
        AnzahlSchere += 1
        if i[0] in Papier:
            Punktzahl2 += 6
            Siege += 1
        elif i[0] in Schere:
            Punktzahl2 += 3
        else: #Stein
            Niederlagen += 1

Punktzahl = Punktzahl1 + Punktzahl2

print(f"Punkte ohne S/U/N: {Punktzahl1}\n"
      f"Stein: {AnzahlStein} Papier: {AnzahlPapier} Schere: {AnzahlSchere}\n"
      f"Punkte ohne Schere, Stein, Papier: {Punktzahl2}\n"
      f"S/U/N: {Siege}/{Unentschieden}/{Niederlagen}\n"
      f"Gesamtpunktzahl: {Punktzahl}")

#---------------------------------------------------------------------------------------

EchtePunktzahl = 0
for i in alleZüge:
    if i[2] == "Z":
        EchtePunktzahl += 6
        if i[0] in Stein: #-> Papier
            EchtePunktzahl += 2
        elif i[0] in Papier: #-> Schere
            EchtePunktzahl += 3
        else: #-> Stein
            EchtePunktzahl += 1
    elif i[2] == "Y":
        EchtePunktzahl += 3
        if i[0] in Stein: #-> Stein
            EchtePunktzahl += 1
        elif i[0] in Papier: #-> Papier
            EchtePunktzahl += 2
        else: #-> Schere
            EchtePunktzahl += 3
    else: # X -> Niederlage
        if i[0] in Stein: #-> Schere
            EchtePunktzahl += 3
        elif i[0] in Papier: #-> Stein
            EchtePunktzahl += 1
        else: #-> Papier
            EchtePunktzahl += 2

print(f"\nrichtige Gesamtpunktzahl: {EchtePunktzahl}")