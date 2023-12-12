#izveidot vārdnīcu ar datiem par automašīnu(4)
auto = {
    "Zīmols" : "Audi",
    "Modelis" : "A4",
    "Motora Tilpums" : 2.5,
    "Krāsa" : "Melna",
    "Gads" : 2018
}

dati = input("Ievadiet zīmolu, lai pārbaudītu: ")
if dati == auto["Zīmols"]:
    print("🚗 ir vārdnīcā")
elif dati == auto.values():
    print("🚗 ir kā vērtība")
else:
    print("Šāda 🚗 nav")