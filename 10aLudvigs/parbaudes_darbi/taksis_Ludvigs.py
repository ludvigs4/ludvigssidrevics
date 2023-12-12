import random

noligsanas_cena = 1.2
dienas_tarifs = 0.47
nakts_tarifs = 0.87
gaidisanas_cena = 0.15
izsaukuma_cena = 2.4    # cenas par taksi

summa = 0.0
nobraukts = 0.0
nogaidits = 0.0 #rēķināmie lielumi

pasazieru_skaits = int(input("Cik būs pasažieri(max 4)?"))
pulkstenis = 0
izbrauksanas_cena = 0.0
brauksanas_summa = 0.0 #čeka lielumi

atlauj_veikala = random.randint(0, 1)#random lielumi ko šoferis iebilst
atlauj_est = random.randint(0, 1)
vai_ed = input("Vai jums ir ēdiens līdzi?:(j/n)")
var_braukt = True
if atlauj_est == 1 and vai_ed == "j":
    var_braukt = False
else:
    var_braukt = True

if pasazieru_skaits <= 4 and var_braukt:   #vai pasažieru skaits ir mazāks par 4?
    pulkstens = int(input("Cikos jūs saucat taksi?"))
    izsaukums = input("Vai jūs braucat no stacijas?(j/n)")
    
    if pulkstenis >= 25:
        pulkstenis = 24

    if izsaukums == "j":
        taksi_stacija = input("Vai stacijā ir kāds taksis?(j/n)")
        if taksi_stacija == "j":
            summa += noligsanas_cena #tiek pieskaitīta nolīgšanas cena
            izbrauksanas_cena = noligsanas_cena
        else:
            summa += izsaukuma_cena
            izbrauksanas_cena = izsaukuma_cena
    else:
        summa += izsaukuma_cena #tiek pieskaitīta izsaukuma cena
        izbrauksanas_cena = izsaukuma_cena

    gaidisana = input("Vai jūs vēlaties ieiet veikalā?(j/n)")

    if gaidisana == "j":
        if atlauj_veikala == 0:
            nogaidits = float(input("Cik minūtes jūs kavēsities veikalā?"))
            summa += gaidisanas_cena * nogaidits #izrēķina cik ir jāmaksā par gaidīšanu
        else:
            print("Šoferis neatļauj iet veikalā!")
    
    nobraukts = float(input("Cik km jūs braucat ar taksometru?"))
    if pulkstenis > 23 or pulkstenis <= 5:  #cikos brauc un izrēķina cik jāmaksā par taksi
        summa += nobraukts * nakts_tarifs
        brauksanas_summa = nobraukts * nakts_tarifs
    else:
        summa += nobraukts * dienas_tarifs
        brauksanas_summa = nobraukts * dienas_tarifs

    print("\n\nCena par izsaukumu:", round(izbrauksanas_cena, 3))
    print("Cena par braukšanu:", round(brauksanas_summa, 3), "EUR", "EUR -", nobraukts, "km")
    print("Cena par stāvēšanu:", round(nogaidits * gaidisanas_cena, 3), "EUR -", nogaidits, "min")
    print("Cena kopā:", round(summa, 3), "EUR")

elif var_braukt and pasazieru_skaits >= 5:
    print("Pasažieri ir pārāk daudz!")
elif var_braukt == False and pasazieru_skaits < 5:
    print("Šoferis neatļauj ēst taksometrā!")
else:
    print("Jums ir pārāk daudz pasažieru un šoferis neatļauj ēst taksometrā!")