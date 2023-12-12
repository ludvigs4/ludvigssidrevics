import math

linoleja_daudzumi = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
kopejais_linoleja_daudzums = 0.00

izmaksas_kopejas = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
kopsumma = 0.00

atlikusie_linoleji = [] #ja vairākas reizes rēķinās, tad te glabāsies dati ievadītie katru reizi
atlikumi = 0.00 #kopējais atlikušais linolejs

izvele1 = False #nodrošina, lai pirmajā reizē neprasa izvēlēties vai rēķinās

while True:
    if izvele1: #prasa vai otru reizi viņu grib rēķināt
        izvele = input('\nVai vēlaties rēķināt? (j/n): ')

        if izvele.lower() != 'n' and izvele.lower() != 'j': #nekorekti dati
            print('Nekorekti dati')
            exit()

        if izvele.lower() == 'n':
            break

    linolejs_cena = float(input('Ievadi linoleja cenu par m²: '))
    rulla_platums = float(input('Ievadi ruļļa platumu: '))
    rulla_garums = float(input('Ievadi ruļļa garumu: '))
    rulla_platiba = rulla_platums*rulla_garums
    istabas_garums = float(input('Ievadi istabas garumu: '))
    istabas_platums = float(input('Ievadi istabas platumu: '))
    istabas_platiba = istabas_garums*istabas_platums
    linoleja_daudzums = istabas_platiba
    izmaksas_linolejs = (math.ceil(linoleja_daudzums))*linolejs_cena #noapaļo linoeja izmaksas
    atlikusais_linolejs = rulla_platiba-istabas_platiba

    linoleja_daudzumi.append(linoleja_daudzums) #pievieno pie augšējā saraksta
    kopejais_linoleja_daudzums+=linoleja_daudzums

    izmaksas_kopejas.append(izmaksas_linolejs) #pievieno pie augšējā saraksta
    kopsumma+=izmaksas_linolejs

    atlikusie_linoleji.append(atlikusais_linolejs) #pievieno pie augšējā saraksta
    atlikumi+=atlikusais_linolejs

    izvele1 = True #pēc pirmās reizes, lai atkārtotos

print("\n--------------------------------------\n")
for i, num in enumerate(linoleja_daudzumi, start=1): #uzraksta linoleja daudzumu katru reizi
    print(f'Linoleja daudzums {i}: {round(num, 2)} m²')
print(f'Kopējais linoleja daudzums ir {round(kopejais_linoleja_daudzums, 2)} m²') #kopējais linoleja daudzums

print("\n--------------------------------------\n")

for i, num in enumerate(izmaksas_kopejas, start=1): #uzraksta linoleja izmaksas katru reizi
    print(f'Izmaksas {i}: {round(num, 2)} EUR')
print(f'Kopsumma šim pirkumam ir {round(kopsumma, 2)} EUR') #kopējā linoleja cena

print("\n--------------------------------------\n")

for i, num in enumerate(atlikusie_linoleji, start=1): #linoleja atlikumi katru reizi
    print(f'Atlikušais linolejs {i}: {round(num, 2)} m²')
print(f'Kopā atliek {round(atlikumi, 2)} m² linoleja') #kopējie atlikumi

if atlikumi<0:
    print('\nNepietiek linolejs\n') #pārbauda negatīvās vērtības
else:
    print()