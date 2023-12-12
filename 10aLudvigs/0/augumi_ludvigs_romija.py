augumi = { #augumi cilvēkiem
    "Ludvigs" : 185,
    "Romija" : 172,
    "Gunča" : 184,
    "Gus" : 164,
    "Emīls" : 162,
    "Zints" : 164,
    "Alise" : 167,
    "Toms" : 177,
    "Anrijs" : 184,
    "Jānis" : 165,
    "Elza" : 180
}

print("Jebkurā brīdī rakstiet stop, lai izietu!\n")

for i in augumi: #izdrukā visus cilvēkus ar augumiem
    print(f"{i} : {augumi[i]}")
print("--------------------")

while True:
    izvele = input('Ko vēlaties darīt? \n1-drukāt\n2-pievienot\n3-izdzēst\n')
    if izvele == '1': #izdrukā visus cilvēkus ar augumiem
        
        for i in augumi:
            print(f"{i} : {augumi[i]}")

    elif izvele == '2': #pieliek jaunu cilvēku vārdnīcai
        vards = input("Ievadiet jauno vārdu: ")
        if vards == 'stop':
            break

        elif augumi.get(vards): #ja ir tāda atslēga
            print("Tāds cilvēks jau ir!")
            print("--------------------")
            continue

        augums = int(input("Ievadiet augumu:"))
        if augums == 'stop':
            break
        
        augumi[vards] = augums
        print(f"Jūs pievienojāt {vards} : {augums}")
    
    elif izvele == '3': #izdzēš cilvēku no vārdnīcas
        dzest = input('Ievadiet, kuru cilvēku gribat dzēst?(ja vēlaties dzēst visus - v)')
        if dzest == 'v': #izdzēš visus cilvēkus
            augumi.clear()
        elif dzest == "stop":
            break
        elif augumi.get(dzest): #ja ir tāda atslēga
            print(f"Jūs izdzēsāt {dzest} : {augumi[dzest]}")
            del augumi[dzest]
        else: #ja nav tāda atslēga
            print("Tāda vārda nav!")

    elif izvele == 'stop':
        break

    else: #ja ievada neeksistējošu vērtību
        print("Nav tāda izvēle")
    print("-------------")