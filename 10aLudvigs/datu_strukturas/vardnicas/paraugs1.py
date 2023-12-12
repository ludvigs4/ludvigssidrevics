telefons = {
    "Jānis" : 20342093,
    "Rita" : 23540923,
    "Anna" : 23947239,
    "Juris" : 23572909
}

#Jānim ir 2 telefona numuri
telefons.update({"Jānis":222222222})
print(f"Šis ir Ritas numurs {telefons['Rita']}")
print(f"Šis ir Jāņa numurs {telefons['Jānis']}")
print(f"Šis ir Annas numurs {telefons['Anna']}")
print(f"Šis ir Jura numurs {telefons['Juris']}")

#izveidot vārdnīcu ar atslēgu virskni un fromkeys() metodi
#vārdnīca, nenorādot ierakstu vērtības
kk = ("viens", "divi", "trīs")
dd = dict.fromkeys(kk)
print(dd)

val = 0 #šī vēr'tiba būs visai vārdņicai
dd = dict.fromkeys(kk, val)
print(dd)

#izveidot vārdņicu, kas satur sarakstu
valstis = {
    "Somija":["Helsinki", "Tampere", "Rovaniemi"],
    "Norvēģija":["Oslo", "Bergena", "Trumse"],
    "Dānija":["Kopengāgena", "Ronne","Odense"]
}
print()
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega, i))
    print("------------------💀")