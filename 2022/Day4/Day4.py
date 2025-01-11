with open('Data - Day 4') as f:
    IDs = f.readlines()

DoppelteZuordnungen = 0

for i in IDs:
    Zuordnung = i.strip()
    Geteilt = Zuordnung.split(",")
    Elf1, Elf2 = Geteilt[0], Geteilt[1]
    Sektoren1, Sektoren2 = Elf1.split("-"), Elf2.split("-")
    Sektor1, Sektor2, Sektor3, Sektor4 = int(Sektoren1[0]), int(Sektoren1[1]), int(Sektoren2[0]), int(Sektoren2[1])
    Bereich1, Bereich2 = list(range(Sektor1, Sektor2+1)), list(range(Sektor3, Sektor4+1))
    if all(Sektor in Bereich1 for Sektor in Bereich2) or all(Sektor in Bereich2 for Sektor in Bereich1):
        DoppelteZuordnungen += 1
        # print("Duplikat!")
    else:
        # print("kein Duplikat")
        continue
print(f"Komplette Doppelte Zuordnungen: {DoppelteZuordnungen}")

# ----------------------------------------------------------------

DoppelteZuordnungen = 0

for i in IDs:
    Zuordnung = i.strip()
    Geteilt = Zuordnung.split(",")
    Elf1, Elf2 = Geteilt[0], Geteilt[1]
    Sektoren1, Sektoren2 = Elf1.split("-"), Elf2.split("-")
    Sektor1, Sektor2, Sektor3, Sektor4 = int(Sektoren1[0]), int(Sektoren1[1]), int(Sektoren2[0]), int(Sektoren2[1])
    Bereich1, Bereich2 = list(range(Sektor1, Sektor2+1)), list(range(Sektor3, Sektor4+1))
    if any(Sektor in Bereich1 for Sektor in Bereich2) or any(Sektor in Bereich2 for Sektor in Bereich1):
        DoppelteZuordnungen += 1
        # print("Duplikat!")
    else:
        # print("kein Duplikat")
        continue

print(f"Doppelte Zuordnungen: {DoppelteZuordnungen}")
