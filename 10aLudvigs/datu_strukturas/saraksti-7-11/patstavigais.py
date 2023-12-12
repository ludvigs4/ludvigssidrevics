#izveidot 3 sarakstus. Lietotājs pats norādīs,
#cik elementus likt sarakstā.
#1. un 2. saraksta vērtības ievada lietotājs
#Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus.
#Katra saraksta saturu glīti parādīt uz ekrāna.

list1 = []
list2 = []
list3 = []

len1 = int(input("Cik lieli būs saraksti?"))
print("------1. saraksts------")
for i in range(len1):
    list1.append(int(input(f"Kāda ir jūsu {i+1}. vērtība?")))

print("------2. saraksts------")
for i in range(len1):
    list2.append(int(input(f"Kāda ir jūsu {i+1}. vērtība?")))
print("-----------------------")
print("Pirmais saraksts: ", end="")
for i in list1:
    print(i, end=" ")
print()

print("Otrais saraksts: ", end="")
for i in list2:
    print(i, end=" ")
print()

print("Trešais saraksts: ", end="")
for i in range(len1):
    list3.append(list1[i] + list2[i])
    print(list3[i], end=" ")