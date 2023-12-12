skaitli = [] #Izveido sarakstu ar skaitļiem, kurus ievadīs.
skaits = 0 #Izveido mainīgo, kurā ievadīs cik skaitļi būs sarakstā.

while skaits < 3: #Kamēr skaits nav >= 3, tikmēr prasa ievadīt citu skaitli.
    skaits = int(input("Ievadiet skaitļu skaitu (ne mazāk kā 3): "))

for i in range(skaits): #Cikls iet cauri tik reizes, cik ievadīts.
    skaitli.append(int(input(f"Ievadiet {i+1}. skaitli: "))) #Pie skaitļu virknes pievieno lietotāja ievadīto skaitli.

print(f"Saraksts ar skaitļiem: {skaitli}")
print(f"Lielākais ievadītais skaitlis ir: {max(skaitli)}")