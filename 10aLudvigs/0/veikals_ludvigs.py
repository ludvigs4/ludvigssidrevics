preces = []
cenas = []
skaits = []
veikali = ["Rimi", "Maxima", "Lidl", "Top", "Elvi"]

karte = False
atlaide = 0
kata_otra = False

summa = 0
grib_ceku = "n"

veikals = int(input("Kādā veikalā jūs iepērkaties?(1 - Rimi, 2 - Maxima, 3 - Lidl, 4 - Top, 5 - Elvi)"))

if veikals < 1 or veikals > 5:
    print("Šāds veikals neeksistē!")
    exit()
if veikals < 3:
    inpt = input("Vai jums ir klientu karte?(1-ir/2-nav)")
    if inpt == "j":
        karte = True

if veikals == 1 and karte == True:
    atlaide = 40
elif veikals == 2 and karte == False:
    atlaide = 20
elif veikals == 2 and karte:
    atlaide = 50
elif veikals == 4:
    kata_otra = True
elif veikals == 5:
    atlaide = 30

while grib_ceku != "j":
    precu_skaits = int(input("Cik preces jūs vēlaties pirkt?:"))
    if precu_skaits <= 0:
        print("Jūs nevarat pirkt mazāk par vienu preci!")
        exit()
    
    prece = input("Kāda ir jūsu prece?")
    cena = float(input("Cik maksā šī prece?"))
    preces.append(prece)
    cenas.append(cena * precu_skaits)
    skaits.append(precu_skaits)

    grib_ceku = input("Vai jūs gribat čeku vai turpināt iepirkties?(j - čeks/n - turpināt)")

if veikals == 3 and len(preces) >= 3:#ja veikals ir lidl un ir vairāk par 3 precēm tad atlaide ir 30
    atlaide = 30

if veikals != 4:
    for i in range(len(preces)):#pieskaita cenas
        cenas[i] = cenas[i] - cenas[i]*atlaide/100
        summa += cenas[i]
else:
    for i in range(len(cenas)):
        if i + 1 % 2 == 0:
            cenas[i] = 0
        summa += cenas[i]


#čeks ------------------------------


print("\n\n\t"+veikali[veikals - 1])
if veikals != 4:
    print(f"Jums pienākas {atlaide}% atlaide")
else:
    print("Jums katra otrā prece ir par brīvu!")
print("-------------------------")
for i in range(len(preces)):
    print(preces[i], f"x{skaits[i]}", "\n\t\t", round(cenas[i], 2), "EUR")
print("-------------------------")
print(f"Kopsumma \t{round(summa,2)}EUR")