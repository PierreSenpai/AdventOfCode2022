with open('Data - Day 7') as f:
    Konsole = f.readlines()

Ordnersystem = {"/":{}}

AktuellerOrdner = AlterOrdner1 = AlterOrdner2 = AlterOrdner3 = AlterOrdner4 = AlterOrdner5 = AlterOrdner6 = AlterOrdner7 = AlterOrdner8 = ""
alleOrdner = {}

DictionaryType = type({})
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


while Konsole:
    BefehlEingegeben = False
    ErgebnisAngezeigt = False
    Befehl = []
    try:
        while not BefehlEingegeben:
            if Konsole[0][0] == "$":
                Befehl.append(Konsole.pop(0).rstrip())
                # print(f"Befehl hinzugefügt: {Befehl}")
            else:
                BefehlEingegeben = True
        while not ErgebnisAngezeigt:
            if Konsole[0][0] == "$":
                ErgebnisAngezeigt = True
            else:
                Befehl.append(Konsole.pop(0).rstrip())
                # print(f"Befehl hinzugefügt: {Befehl}")
        # print(f"Befehl: {Befehl}")
    except:
        pass
    for i in Befehl:
        if i[0] == "$":
            Parameter = i.split()
            if Parameter[1] == "cd":
                if Parameter[2] == "..":
                    AktuellerOrdner = AlterOrdner1
                    AlterOrdner1 = AlterOrdner2
                    AlterOrdner2 = AlterOrdner3
                    AlterOrdner3 = AlterOrdner4
                    AlterOrdner4 = AlterOrdner5
                    AlterOrdner5 = AlterOrdner6
                    AlterOrdner6 = AlterOrdner7
                    AlterOrdner7 = AlterOrdner8
                    AlterOrdner8 = ""
                    # print(f"Ein Ordner zurückgegangen (zu: {AktuellerOrdner})!")
                    # print(
                    #     f"{bcolors.OKCYAN}1:{AlterOrdner1} 2:{AlterOrdner2} 3:{AlterOrdner3} 4:{AlterOrdner4} 5:{AlterOrdner5} 6:{AlterOrdner6} 7:{AlterOrdner7} 8:{AlterOrdner8}{bcolors.ENDC}")
                else:
                    AlterOrdner8 = AlterOrdner7
                    AlterOrdner7 = AlterOrdner6
                    AlterOrdner6 = AlterOrdner5
                    AlterOrdner5 = AlterOrdner4
                    AlterOrdner4 = AlterOrdner3
                    AlterOrdner3 = AlterOrdner2
                    AlterOrdner2 = AlterOrdner1
                    AlterOrdner1 = AktuellerOrdner
                    AktuellerOrdner = Parameter[2]
                    # print(f"Aktuellen Ordner geändert (zu: {AktuellerOrdner})!")
                    # print(f"{bcolors.OKCYAN}1:{AlterOrdner1} 2:{AlterOrdner2} 3:{AlterOrdner3} 4:{AlterOrdner4} 5:{AlterOrdner5} 6:{AlterOrdner6} 7:{AlterOrdner7} 8:{AlterOrdner8}{bcolors.ENDC}")
            # print(f"'{i}' wurde verarbeitet")
        else:
            Parameter = i.split()
            if Parameter[0] == "dir":
                if AlterOrdner8:
                    Ordnersystem[AlterOrdner8][AlterOrdner7][AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][
                        AlterOrdner1][AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 8{bcolors.ENDC}")
                elif AlterOrdner7:
                    Ordnersystem[AlterOrdner7][AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][
                        AlterOrdner1][AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 7{bcolors.ENDC}")
                elif AlterOrdner6:
                    Ordnersystem[AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][
                        AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 6{bcolors.ENDC}")
                elif AlterOrdner5:
                    Ordnersystem[AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][
                        Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 5{bcolors.ENDC}")
                elif AlterOrdner4:
                    Ordnersystem[AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][
                        Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 4{bcolors.ENDC}")
                elif AlterOrdner3:
                    Ordnersystem[AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 3{bcolors.ENDC}")
                elif AlterOrdner2:
                    Ordnersystem[AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 2{bcolors.ENDC}")
                elif AlterOrdner1:
                    Ordnersystem[AlterOrdner1][AktuellerOrdner][Parameter[1]] = {}
                    # print(f"{bcolors.HEADER}Alte Ordner: 1{bcolors.ENDC}")
                else:
                    Ordnersystem[AktuellerOrdner][Parameter[1]] = {}
                #     print(f"{bcolors.HEADER}Alte Ordner: 0{bcolors.ENDC}")
                # print(f"{bcolors.WARNING}{Ordnersystem}{bcolors.ENDC}")
            else:
                if AlterOrdner8:
                    Ordnersystem[AlterOrdner8][AlterOrdner7][AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][
                        AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 8{bcolors.ENDC}")
                elif AlterOrdner7:
                    Ordnersystem[AlterOrdner7][AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 7{bcolors.ENDC}")
                elif AlterOrdner6:
                    Ordnersystem[AlterOrdner6][AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 6{bcolors.ENDC}")
                elif AlterOrdner5:
                    Ordnersystem[AlterOrdner5][AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 5{bcolors.ENDC}")
                elif AlterOrdner4:
                    Ordnersystem[AlterOrdner4][AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 4{bcolors.ENDC}")
                elif AlterOrdner3:
                    Ordnersystem[AlterOrdner3][AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 3{bcolors.ENDC}")
                elif AlterOrdner2:
                    Ordnersystem[AlterOrdner2][AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 2{bcolors.ENDC}")
                elif AlterOrdner1:
                    Ordnersystem[AlterOrdner1][AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 1{bcolors.ENDC}")
                else:
                    Ordnersystem[AktuellerOrdner][Parameter[1]] = Parameter[0]
                    # print(f"{bcolors.HEADER}Alte Ordner: 0{bcolors.ENDC}")
                # print(f"{bcolors.WARNING}{Ordnersystem}{bcolors.ENDC}")
    # print("Befehl abgeschlossen!")

def Ordnercheck(Ordner):
    for k,v in Ordner.items():
        if type(v) == DictionaryType:
            return True, k, v, "Value ist ein Ordner"
    return False, "Value ist kein Ordner"

def SpeicherBerechnen(Ordner):
    if Ordnercheck(Ordner)[0]:
        return False, Ordnercheck(Ordner)[1], Ordnercheck(Ordner)[2]
    SpeicherverbrauchOrdner = 0
    for k,v in Ordner.items():
        SpeicherverbrauchOrdner += int(v)
    return True, SpeicherverbrauchOrdner

# def FindeDasKleinste(Dictionary):
#     while len(Dictionary) > 1:
#         Maximum = Dictionary[Dictionary.keys()[0]]
#         if
#
#     Maximum = 70000000
#     Kleinste = []
#     for k,v in Dictionary.items():
#         if >

# print(Ordnersystem)
GesamtspeicherUnter100k = 0

while type(Ordnersystem["/"]) == DictionaryType:
    # print(f"{bcolors.HEADER}1. while loop angefangen!{bcolors.ENDC}")
    for i in range(1,11):
        locals().__setitem__(f"Ordner{i}", "")
    alterOrdner = 0
    aktuellerOrdner = Ordnersystem
    Ordnertiefe = 0
    while True:
        # print(f"{bcolors.HEADER}2. while loop angefangen!{bcolors.ENDC}")
        Ergebnis = SpeicherBerechnen(aktuellerOrdner)
        # print(f"{bcolors.OKCYAN}Ergebnis der Berechnung: {Ergebnis}{bcolors.ENDC}")
        if Ergebnis[0]:
            # print(f"{bcolors.HEADER}2. while loop abgebrochen!{bcolors.ENDC}")
            break
        # print(f"Alter Ordnerinhalt: {aktuellerOrdner}")
        alterOrdner = aktuellerOrdner
        aktuellerOrdner = aktuellerOrdner[Ergebnis[1]]
        # print(f"Neue Ordner: '{Ergebnis[1]}' mit Inhalt: {Ergebnis[2]}")
        Ordnertiefe += 1
        # print(f"neue Ordnertiefe: {Ordnertiefe}")
        locals().__setitem__(f"Ordner{Ordnertiefe}",Ergebnis[1])
    Speicherverbrauch = Ergebnis[1]
    if Speicherverbrauch < 100000:
        GesamtspeicherUnter100k += Speicherverbrauch
    # print(f"Gesamtspeicherverbrauch der Ordner mit weniger als 100.000 Speicherverbrauch: {GesamtspeicherUnter100k}")
    # print(f"Speicherverbrauch des Ordners: {Speicherverbrauch}")
    if Ordnertiefe == 10:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5][Ordner6][Ordner7][Ordner8][Ordner9][Ordner10] = Speicherverbrauch
        alleOrdner[Ordner10] = Speicherverbrauch
    elif Ordnertiefe == 9:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5][Ordner6][Ordner7][Ordner8][Ordner9] = Speicherverbrauch
        alleOrdner[Ordner9] = Speicherverbrauch
    elif Ordnertiefe == 8:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5][Ordner6][Ordner7][Ordner8] = Speicherverbrauch
        alleOrdner[Ordner8] = Speicherverbrauch
    elif Ordnertiefe == 7:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5][Ordner6][Ordner7] = Speicherverbrauch
        alleOrdner[Ordner7] = Speicherverbrauch
    elif Ordnertiefe == 6:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5][Ordner6] = Speicherverbrauch
        alleOrdner[Ordner6] = Speicherverbrauch
    elif Ordnertiefe == 5:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4][Ordner5] = Speicherverbrauch
        alleOrdner[Ordner5] = Speicherverbrauch
    elif Ordnertiefe == 4:
        Ordnersystem[Ordner1][Ordner2][Ordner3][Ordner4] = Speicherverbrauch
        alleOrdner[Ordner4] = Speicherverbrauch
    elif Ordnertiefe == 3:
        Ordnersystem[Ordner1][Ordner2][Ordner3] = Speicherverbrauch
        alleOrdner[Ordner3] = Speicherverbrauch
    elif Ordnertiefe == 2:
        Ordnersystem[Ordner1][Ordner2] = Speicherverbrauch
        alleOrdner[Ordner2] = Speicherverbrauch
    elif Ordnertiefe == 1:
        Ordnersystem[Ordner1] = Speicherverbrauch
        alleOrdner[Ordner1] = Speicherverbrauch

print(f"Gesamtspeicherverbrauch der Ordner mit weniger als 100.000 Speicherverbrauch: {GesamtspeicherUnter100k}")
benötigterSpeicher = Ordnersystem["/"]-40000000
print(f"alle Ordner: {alleOrdner}")
alleOrdnerGroß = {}
for k,v in alleOrdner.items():
    if v >= benötigterSpeicher:
        alleOrdnerGroß[k] = v
    # print("Erfolgreich")
print(f"alle Ordner über 100.000: {alleOrdnerGroß}")

Maximum = 70000000
for k,v in alleOrdnerGroß.items():
    if v < Maximum:
        Maximum = v

print(Maximum)

