to_do_list = {
    'nosaukums' : [],
    "termiņš" : [],
    "statuss" : []
}

while True:
    izvele = int(input('Ko vēlaties darīt? \n1-pievienot jaunu darbu\n2-izdzēst darbu\n3-nomainīt statusu\n4-drukāt darbus\n'))

    if izvele == 1:
        pievienot = input('Pievieno darba nosaukumu: ')
        to_do_list['nosaukums'].append(pievienot)
        termins = input('Pievieno termiņu(piemēram, 12.12.2023): ')
        to_do_list["termiņš"].append(termins)
        to_do_list['statuss'].append(True)

    elif izvele == 2:
        dzest = input("Ierakstiet darba nosaukumu, kuru vēlaties dzēst: ")
        indeks = to_do_list['nosaukums'].index(dzest)
        del to_do_list['nosaukums'][indeks]
        del to_do_list['termiņš'][indeks]
        del to_do_list['statuss'][indeks]

    elif izvele == 3:
        nosaukums = input("Ierakstiet darba nosaukumu, kuram vēlaties mainīt statusu: ")
        statuss = input("Uz kādu statusu vēlaties pārmainīt?(1-esošs, 2-neesošs)")
        if statuss == "1":
            to_do_list['statuss'][to_do_list['nosaukums'].index(nosaukums)] = True
        elif statuss == "2":
            to_do_list['statuss'][to_do_list['nosaukums'].index(nosaukums)] = False
        else:
            exit()#sakt blaut kkad

    elif izvele == 4:
        for i in range(len(to_do_list['nosaukums'])):
            print(f"{to_do_list['nosaukums'][i]} : {to_do_list['termiņš'][i]} : {to_do_list['statuss'][i]}")
