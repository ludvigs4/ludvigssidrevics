kontakti = {#vārdnīca ar numuriem un vārdiem
    "vards" :["Jānis", "Anna", "Zane", "Gustavs"],
    "numurs": ["20892374", "22323522", "23527930", "22352357"]
}

janis = input('Vai Jums ir Jānis kontaktos?(j/n): ')
if janis == "n":#pārbauda vai ir kontaktos, ja ir tad turpinas, ja nav tad izdzēš
    kontakti["vards"].remove(kontakti["vards"][0])
    kontakti["numurs"].remove(kontakti["numurs"][0])

while True:
    lietotajagajiens= input('Ko vēlaties darīt? \n\t1-drukāt\n\t2-pievienot\n\t3-izdzēst\n\t4-iziet\n')

    if lietotajagajiens == '1':#tiek parādīti kontakti uz ekrāna
        print("Jūs uzspiedāt ataustiņu 1 : jūsu kontakti uz ekrāna:")
        for i in range(len(kontakti['vards'])):
            print(f"Kontakts: {kontakti['vards'][i]} : numurs: {kontakti['numurs'][i]}")
    if lietotajagajiens == '2':#tiek pievienots kontakts
        print("Jūs uzspiedāt taustiņu 2: pievieno kontaktu:")
        vards = input("Ievadiet vārdu:")
        numurs = input("Ievadiet numuru:")
        kontakti["vards"].append(vards)
        kontakti["numurs"].append(numurs)
    elif lietotajagajiens == '3':#tiek izdzēsts kontakts
        print("Jūs uzspiedāt taustiņu 3: izdzēš kontaktu:")
        vards = input("Ievadiet vārdu:")
        index = kontakti["vards"].index(vards)
        kontakti["vards"].remove(vards)
        kontakti["numurs"].remove(kontakti["numurs"][index])
    elif lietotajagajiens == "4":#beidzas programma
        print("Jūs uzspiedāt taustiņu 4: Paldies, ka izmantojāt šo programmu!")
        break