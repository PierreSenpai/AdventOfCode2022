# with open('Data - Day 9') as f:
#     Bewegungen = f.readlines()
#
# gitterlänge = 200
#
# gitter = {}
#
# for x in range(gitterlänge+1): #Gitteraufbau
#     for y in range(gitterlänge+1):
#         gitter[f"{x}|{y}"] = []
#     for y in range(gitterlänge + 1):
#         gitter[f"{x}|{-y}"] = []
#     for y in range(gitterlänge+1):
#         gitter[f"{-x}|{y}"] = []
#     for y in range(gitterlänge + 1):
#         gitter[f"{-x}|{-y}"] = []
#
# besuchtefelder = gitter
# gitter["0|0"] = ["T","H"]
#
# xKoordinate, yKoordinate = 0, 0
#
# def Prüfen(xH,yH):
#     for x in range(2):
#         for y in range(2):
#             if "T" in gitter[f"{xH+x}|{yH+y}"]:
#                 return True
#             if "T" in gitter[f"{xH+x}|{yH-y}"]:
#                 return True
#             if "T" in gitter[f"{xH-x}|{yH+y}"]:
#                 return True
#             if "T" in gitter[f"{xH-x}|{yH-y}"]:
#                 return True
#     return False
#
# def TailFinden():
#     for k,v in gitter.items():
#         if "T" in v:
#             xKoordinateTail = int(k.split("|")[0])
#             yKoordinateTail = int(k.split("|")[1])
#             return xKoordinateTail,yKoordinateTail
#
# def HeadEntfernen():
#     for k,v in gitter.items():
#         if "H" in v:
#             x = k.split("|")[0]
#             y = k.split("|")[1]
#     gitter[f"{x}|{y}"].remove("H")
#     # print("Head entfernt")
#
# def StelleMarkieren():
#     besuchtefelder[f"{TailFinden()[0]}|{TailFinden()[1]}"].append("#")
#
# for Bewegung in Bewegungen:
#     Richtung = Bewegung.split()[0]
#     Schritte = int(Bewegung.split()[1])
#     if Richtung == "U":
#         for Anzahl in range(Schritte):
#             HeadEntfernen()
#             xKoordinateTail = TailFinden()[0]
#             yKoordinateTail = TailFinden()[1]
#             yKoordinate += 1
#             gitter[f"{xKoordinate}|{yKoordinate}"].append("H")
#             if not Prüfen(xKoordinate,yKoordinate):
#                 gitter[f"{xKoordinateTail}|{yKoordinateTail}"].remove("T")
#                 if xKoordinate == xKoordinateTail:
#                     if yKoordinate > yKoordinateTail:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail+1}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail-1}"].append("T")
#                         StelleMarkieren()
#                 elif yKoordinate == yKoordinateTail:
#                     if xKoordinate > xKoordinateTail:
#                         gitter[f"{xKoordinateTail+1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail-1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                 else:
#                     if xKoordinate > xKoordinateTail:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail+1}|{yKoordinateTail+1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail+1}|{yKoordinateTail-1}"].append("T")
#                             StelleMarkieren()
#                     else:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail-1}|{yKoordinateTail+1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail-1}|{yKoordinateTail-1}"].append("T")
#                             StelleMarkieren()
#     elif Richtung == "D":
#         for Anzahl in range(Schritte):
#             # print("DOWN for loop")
#             HeadEntfernen()
#             xKoordinateTail = TailFinden()[0]
#             yKoordinateTail = TailFinden()[1]
#             yKoordinate += -1
#             gitter[f"{xKoordinate}|{yKoordinate}"].append("H")
#             if not Prüfen(xKoordinate, yKoordinate):
#                 gitter[f"{xKoordinateTail}|{yKoordinateTail}"].remove("T")
#                 if xKoordinate == xKoordinateTail:
#                     if yKoordinate > yKoordinateTail:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail + 1}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail - 1}"].append("T")
#                         StelleMarkieren()
#                 elif yKoordinate == yKoordinateTail:
#                     if xKoordinate > xKoordinateTail:
#                         gitter[f"{xKoordinateTail + 1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail - 1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                 else:
#                     if xKoordinate > xKoordinateTail:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail + 1}|{yKoordinateTail + 1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail + 1}|{yKoordinateTail - 1}"].append("T")
#                             StelleMarkieren()
#                     else:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail - 1}|{yKoordinateTail + 1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail - 1}|{yKoordinateTail - 1}"].append("T")
#                             StelleMarkieren()
#     elif Richtung == "R":
#         for Anzahl in range(Schritte):
#             # print("RIGHT For loop")
#             HeadEntfernen()
#             xKoordinateTail = TailFinden()[0]
#             yKoordinateTail = TailFinden()[1]
#             xKoordinate += 1
#             gitter[f"{xKoordinate}|{yKoordinate}"].append("H")
#             if not Prüfen(xKoordinate,yKoordinate):
#                 gitter[f"{xKoordinateTail}|{yKoordinateTail}"].remove("T")
#                 if xKoordinate == xKoordinateTail:
#                     if yKoordinate > yKoordinateTail:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail+1}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail-1}"].append("T")
#                         StelleMarkieren()
#                 elif yKoordinate == yKoordinateTail:
#                     if xKoordinate > xKoordinateTail:
#                         gitter[f"{xKoordinateTail+1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail-1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                 else:
#                     if xKoordinate > xKoordinateTail:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail+1}|{yKoordinateTail+1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail+1}|{yKoordinateTail-1}"].append("T")
#                             StelleMarkieren()
#                     else:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail-1}|{yKoordinateTail+1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail-1}|{yKoordinateTail-1}"].append("T")
#                             StelleMarkieren()
#     elif Richtung == "L":
#         for Anzahl in range(Schritte):
#             # print("LEFT For loop")
#             HeadEntfernen()
#             xKoordinateTail = TailFinden()[0]
#             yKoordinateTail = TailFinden()[1]
#             xKoordinate += -1
#             gitter[f"{xKoordinate}|{yKoordinate}"].append("H")
#             if not Prüfen(xKoordinate, yKoordinate):
#                 gitter[f"{xKoordinateTail}|{yKoordinateTail}"].remove("T")
#                 if xKoordinate == xKoordinateTail:
#                     if yKoordinate > yKoordinateTail:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail + 1}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail}|{yKoordinateTail - 1}"].append("T")
#                         StelleMarkieren()
#                 elif yKoordinate == yKoordinateTail:
#                     if xKoordinate > xKoordinateTail:
#                         gitter[f"{xKoordinateTail + 1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                     else:
#                         gitter[f"{xKoordinateTail - 1}|{yKoordinateTail}"].append("T")
#                         StelleMarkieren()
#                 else:
#                     if xKoordinate > xKoordinateTail:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail + 1}|{yKoordinateTail + 1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail + 1}|{yKoordinateTail - 1}"].append("T")
#                             StelleMarkieren()
#                     else:
#                         if yKoordinate > yKoordinateTail:
#                             gitter[f"{xKoordinateTail - 1}|{yKoordinateTail + 1}"].append("T")
#                             StelleMarkieren()
#                         else:
#                             gitter[f"{xKoordinateTail - 1}|{yKoordinateTail - 1}"].append("T")
#                             StelleMarkieren()
#
# # print(gitter)
# besuchtefelder["0|0"].append("#")
# # print(besuchtefelder)
# AnzahlBesuchteFelder = 0
# for k,v in besuchtefelder.items():
#     if "#" in v:
#         AnzahlBesuchteFelder += 1
#
# print(AnzahlBesuchteFelder)
# --------------------------------------------------------------------------
with open('Data - Day 9') as f:
    Bewegungen = f.readlines()


def KoordinatenFinden(Knoten):
    for k,v in gitter.items():
        if Knoten in v:
            # print(f"Koordinaten:{k}")
            # print("Knoten gefunden")
            return int(k.split("|")[0]),int(k.split("|")[1])
def PunktVerschieben(Punkt,x,y,Richtung):
    gitter[f"{x}|{y}"].remove(Punkt)
    if Richtung == "U":
        gitter[f"{x}|{y+1}"].append(Punkt)
    elif Richtung == "D":
        gitter[f"{x}|{y-1}"].append(Punkt)
    elif Richtung == "R":
        gitter[f"{x+1}|{y}"].append(Punkt)
    elif Richtung == "L":
        gitter[f"{x-1}|{y}"].append(Punkt)
    elif Richtung == "++":
        gitter[f"{x+1}|{y+1}"].append(Punkt)
    elif Richtung == "+-":
        gitter[f"{x+1}|{y-1}"].append(Punkt)
    elif Richtung == "-+":
        gitter[f"{x-1}|{y+1}"].append(Punkt)
    elif Richtung == "--":
        gitter[f"{x-1}|{y-1}"].append(Punkt)
def Prüfen(Punkt,x,y):
    for xDistanz in range(2):
        for yDistanz in range(2):
            if Punkt in gitter[f"{x+xDistanz}|{y+yDistanz}"]:
                return True
            if Punkt in gitter[f"{x+xDistanz}|{y-yDistanz}"]:
                return True
            if Punkt in gitter[f"{x-xDistanz}|{y+yDistanz}"]:
                return True
            if Punkt in gitter[f"{x-xDistanz}|{y-yDistanz}"]:
                return True
    return False
def RichtungFinden(x,y,xZiel,yZiel):
    if x == xZiel:
        if y < yZiel:
            return "U"
        else:
            return "D"
    if y == yZiel:
        if x < xZiel:
            return "R"
        else:
            return "L"
    if x < xZiel:
        if y < yZiel:
            return "++"
        else:
            return "+-"
    else:
        if y < yZiel:
            return "-+"
        else:
            return "--"


gitterlänge = 200 # Gitter erstellen
gitter = {}
for x in range(gitterlänge+1): #Gitteraufbau
    for y in range(gitterlänge+1):
        gitter[f"{x}|{y}"] = []
    for y in range(gitterlänge + 1):
        gitter[f"{x}|{-y}"] = []
    for y in range(gitterlänge+1):
        gitter[f"{-x}|{y}"] = []
    for y in range(gitterlänge + 1):
        gitter[f"{-x}|{-y}"] = []
besuchtefelder = gitter.copy()
gitter["0|0"] = [0,1,2,3,4,5,6,7,8,9]
besuchtefelder["0|0"] = ["#"]

AnzahlBewegung = 0
for Bewegung in Bewegungen:
    Schritte = int(Bewegung.split()[1])
    for Schritt in range(Schritte):
        Richtung = Bewegung.split()[0]
        for Knoten in range(10):
            xKoordinate = KoordinatenFinden(Knoten)[0]
            yKoordinate = KoordinatenFinden(Knoten)[1]
            if Knoten == 0:
                PunktVerschieben(Knoten,xKoordinate,yKoordinate,Richtung)
            else:
                if not Prüfen(Knoten-1,xKoordinate,yKoordinate):
                    xZiel = KoordinatenFinden(Knoten-1)[0]
                    yZiel = KoordinatenFinden(Knoten-1)[1]
                    Richtung = RichtungFinden(xKoordinate,yKoordinate,xZiel,yZiel)
                    PunktVerschieben(Knoten,xKoordinate,yKoordinate,Richtung)
            if Knoten == 9:
                x = KoordinatenFinden(Knoten)[0]
                y = KoordinatenFinden(Knoten)[1]
                besuchtefelder[f"{x}|{y}"].append("#")
    AnzahlBewegung += 1
    print(AnzahlBewegung)

AnzahlBesuchteFelder = 0
for k,v in besuchtefelder.items():
    if "#" in v:
        AnzahlBesuchteFelder += 1
        print(AnzahlBesuchteFelder)

# print(AnzahlBesuchteFelder)
