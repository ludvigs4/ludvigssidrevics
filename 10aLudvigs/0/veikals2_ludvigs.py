preces = []
cenas = []
cenas_ar_atlaidi = []
skaits = []
veikali = ["Rimi", "Maxima", "Lidl", "Top", "Elvi"]

karte = False
atlaide = 1
kata_otra = False

summa = 0
summa_ar_atlaidi = 0
vajag_ceku = "n"

print("Kādā veikalā jūs iepērkaties?")
print("1 - Rimi - 10% atlaide un 50% ar karti")
print("2 - Maxima - 20% atlaide un 40% ar karti")
print("3 - Lidl - 30% atlaide")
print("4 - Top - 40% atlaide ja nopirktas 3 un vairāk preces")
print("5 - Elvi - Ja pirkuma cena ir 5 vai vairāk EUR tad katra otrā prece par brīvu")
veikals = int(input())


if veikals < 1 or veikals > 5:
    print("Šāds veikals neeksistē!")
    exit()

while vajag_ceku == "n":
    prece = input("Kādu preci jums vajag?")
    preces_cena = float(input("Cik maksā šī prece?"))

    preces.append(prece)
    cenas.append(preces_cena)
    summa += preces_cena

    vajag_ceku = input("Vai jūs esat pabeidzis iepirkties?(j/n)")

if veikals <= 2:
    inpt = input("Vai jums ir karte?(j/n)")
    if inpt == "j":
        karte = True

if veikals == 1:
    if karte:
        atlaide = 50
    else:
        atlaide = 10
if veikals == 2:
    if karte:
        atlaide = 40
    else:
        atlaide = 20
if veikals == 3:
    atlaide = 30
if veikals == 4 and len(preces) >= 3:
    atlaide = 40
if veikals == 5 and summa >= 5:
    kata_otra = True
    for i in range(len(preces)):
        if i % 2 == 0:
            cenas[i] == 0
        summa_ar_atlaidi += cenas[i]

if veikals != 5:
    for i in range(len(cenas)):
        cenas_ar_atlaidi.append(cenas[i] * (100-atlaide) / 100)
        summa_ar_atlaidi += cenas_ar_atlaidi[i]

#čeks-----------------------------

print("\n\n\t"+veikali[veikals - 1])
if veikals != 5:
    print(f"Jums pienākas {atlaide}% atlaide")
elif kata_otra:
    print("Katra otrā prece ir par brīvu!")
print("-------------------------------")
for i in range(len(preces)):
    print(preces[i], "\t\t", round(cenas[i], 2), "EUR")
print("-------------------------------")
print(f"summa bez atlaides {summa}EUR")
print(f"summa ar atlaidi {summa_ar_atlaidi}EUR")