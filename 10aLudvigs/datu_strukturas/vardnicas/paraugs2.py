valstis = {
    "Somija":["Helsinki", "Tampere", "Rovaniemi", "Kemijarvi", "Jyvaskyle"],
    "Norvēģija":["Oslo", "Bergena", "Trumse", "Arendāla", "Molde"],
    "Dānija":["Kopengāgena", "Ronne","Odense", "Aarhus", "Kopenhāgena2"]
}

#izdrukāt vārdnīcas elementus, piekļūstot vārdnīcā konkrētajai atslēgai
for i in valstis["Dānija"]:
    print(i, "\n------------------💀💀💀")
for i in valstis["Norvēģija"]:
    print(i, "\n------------------💀💀💀")
for i in valstis["Somija"]:
    print(i, "\n------------------💀💀💀")


print(valstis["Somija"][:3])
print(valstis["Norvēģija"][:3])
print(valstis["Dānija"][:3])

print(valstis["Norvēģija"][-2:])
print(valstis["Somija"][:-3])
print(valstis["Dānija"][1:5])