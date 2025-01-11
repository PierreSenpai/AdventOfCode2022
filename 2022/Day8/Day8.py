with open('Data - Day 8') as f:
    Gitterliste = f.readlines()

Koordinatenliste = {}
sichtbareBäume = 0
MengeReihe = len(Gitterliste)
MengeSpalte = len(Gitterliste[0].rstrip())

for Reihenzahl in range(MengeReihe):
    Reihe = Gitterliste[Reihenzahl].rstrip()
    for Spaltenzahl in range(MengeSpalte):
        Baumhöhe = Reihe[Spaltenzahl]
        Koordinatenliste[f"{Spaltenzahl+1}-{Reihenzahl+1}"] = Baumhöhe

def CheckOben(Spalte,Reihe,Höhe):
    for Reihenzahl in range(1,int(Reihe)):
        if int(Koordinatenliste[f"{Spalte}-{Reihenzahl}"]) >= Höhe:
            return False, f"{Spalte}-{Reihenzahl}", int(Koordinatenliste[f"{Spalte}-{Reihenzahl}"])
    return True, Spalte,Reihe,Höhe, "Oben"
def CheckUnten(Spalte,Reihe,Höhe):
    for Reihenzahl in range(int(Reihe)+1,MengeReihe+1):
        if int(Koordinatenliste[f"{Spalte}-{Reihenzahl}"]) >= Höhe:
            return False, f"{Spalte}-{Reihenzahl}", int(Koordinatenliste[f"{Spalte}-{Reihenzahl}"])
    return True, Spalte,Reihe,Höhe, "Unten"
def CheckLinks(Spalte,Reihe,Höhe):
    for Spaltenzahl in range(1,int(Spalte)):
        if int(Koordinatenliste[f"{Spaltenzahl}-{Reihe}"]) >= Höhe:
            return False, f"{Spaltenzahl}-{Reihe}", int(Koordinatenliste[f"{Spaltenzahl}-{Reihe}"])
    return True, Spalte,Reihe,Höhe, "Links"
def CheckRechts(Spalte,Reihe,Höhe):
    for Spaltenzahl in range(int(Spalte)+1,MengeSpalte+1):
        if int(Koordinatenliste[f"{Spaltenzahl}-{Reihe}"]) >= Höhe:
            return False, f"{Spaltenzahl}-{Reihe}", int(Koordinatenliste[f"{Spaltenzahl}-{Reihe}"])
    return True, Spalte,Reihe,Höhe, "Rechts"
def SichtbarCheck(Spalte,Reihe,Höhe):
    if CheckOben(Spalte,Reihe,Höhe)[0]:
        return CheckOben(Spalte,Reihe,Höhe)
    if CheckUnten(Spalte,Reihe,Höhe)[0]:
        return CheckUnten(Spalte,Reihe,Höhe)
    if CheckLinks(Spalte,Reihe,Höhe)[0]:
        return CheckLinks(Spalte,Reihe,Höhe)
    if CheckRechts(Spalte,Reihe,Höhe)[0]:
        return CheckRechts(Spalte,Reihe,Höhe)
    return False, Spalte, Reihe, Höhe

for k,v in Koordinatenliste.items():
    Koordinaten = k.split("-")
    Reihe = int(Koordinaten[1])
    Spalte = int(Koordinaten[0])
    if Spalte == 1 or Spalte == MengeSpalte or Reihe == 1 or Reihe == MengeReihe:
        pass
        # print(f"am Rand - Reihe:{Reihe}, Spalte: {Spalte}")
    else:
        if not SichtbarCheck(Spalte,Reihe,int(v))[0]:
            # print("nicht sichtbar")
            # print(SichtbarCheck(Spalte,Reihe,int(v)))
            pass
        else:
            sichtbareBäume += 1
            # print("sichtbar")
            # print((SichtbarCheck(Spalte,Reihe,int(v))))

RandBäume = 2*MengeReihe+2*MengeSpalte-4
sichtbareBäume += RandBäume
print(f"Sichtbare Bäume: {sichtbareBäume}")
#------------------------------------------------------------------------
HöchstePunktzahl = 0

def MengeOben(Spalte,Reihe,Höhe):
    AnzahlSichtbare = 0
    for i in range(1,Reihe):
        if int(Koordinatenliste[f"{Spalte}-{Reihe-i}"]) < Höhe:
            AnzahlSichtbare += 1
        else:
            AnzahlSichtbare += 1
            break
    return AnzahlSichtbare
def MengeUnten(Spalte,Reihe,Höhe):
    AnzahlSichtbare = 0
    for i in range(1,MengeReihe-Reihe+1):
        if int(Koordinatenliste[f"{Spalte}-{Reihe+i}"]) >= Höhe:
            AnzahlSichtbare += 1
            break
        else:
            AnzahlSichtbare += 1
    return AnzahlSichtbare
def MengeLinks(Spalte,Reihe,Höhe):
    AnzahlSichtbare = 0
    for i in range(1,Spalte):
        if int(Koordinatenliste[f"{Spalte-i}-{Reihe}"]) >= Höhe:
            AnzahlSichtbare += 1
            break
        else:
            AnzahlSichtbare += 1
    return AnzahlSichtbare
def MengeRechts(Spalte,Reihe,Höhe):
    AnzahlSichtbare = 0
    for i in range(1,MengeSpalte-Spalte+1):
        if int(Koordinatenliste[f"{Spalte+i}-{Reihe}"]) >= Höhe:
            AnzahlSichtbare += 1
            break
        else:
            AnzahlSichtbare += 1
    return AnzahlSichtbare

for k,v in Koordinatenliste.items():
    Koordinaten = k.split("-")
    Reihe = int(Koordinaten[1])
    Spalte = int(Koordinaten[0])
    if Spalte == 1 or Spalte == MengeSpalte or Reihe == 1 or Reihe == MengeReihe:
        pass
    else:
        Oben = MengeOben(Spalte,Reihe,int(v))
        Unten = MengeUnten(Spalte,Reihe,int(v))
        Links = MengeLinks(Spalte,Reihe,int(v))
        Rechts = MengeRechts(Spalte,Reihe,int(v))
        Punktzahl = Oben * Unten * Links * Rechts
        if Punktzahl > HöchstePunktzahl:
            HöchstePunktzahl = Punktzahl
            # print(f"{Spalte}-{Reihe} größer: {Oben}, {Unten}, {Links}, {Rechts}")
        else:
            pass
            # print(f"{Spalte}-{Reihe} nicht größer: {Oben}, {Unten}, {Links}, {Rechts}")

print(f"Höchste Punktzahl: {HöchstePunktzahl}")
