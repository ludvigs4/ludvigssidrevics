skaitli = [] #Deklarē sarakstu ar skaitļiem, kurus ievadīs.
para = 0 #Mainīgais skaitīs pāra skaitļus un beigās parādīs uz ekrāna.
nepara = 0 #Mainīgais skaitīs nepāra skaitļus un beigās parādīs uz ekrāna.

for i in range(10): #iet cauri ciklam 10 reizes un prasa ievadīt virknes skaitļus.
    skaitli.append(int(input(f"Ievadi {i+1}. skaitli: "))) #Pievieno lietotāja ievadīto skaitli sarakstam.

print(f"saraksts: {skaitli}")

for i in skaitli: #Ciklē cauri sarakstam.
    if i % 2 == 0: #Ja ir pāra skaitlis.
        para += 1 #Pieskaita pāra skaitli.
    else: #Ja ir nepāra skaitlis.
        nepara += 1 #Pieskaita nepāra skaitli.

print(f"Pāra skaitļu skaits: {para}")
print(f"Nepāra skaitļu skaits: {nepara}")