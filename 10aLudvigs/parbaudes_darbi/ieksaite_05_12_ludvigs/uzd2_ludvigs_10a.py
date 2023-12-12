gradi = { #Vārdnīca glabā visas temperatūras un datumus.
    "1.decembris" : -3,
    "2.decembris" : 0,
    "3.decembris" : 7,
    "4.decembris" : 2,
    "5.decembris" : -1,
    "6.decembris" : -4,
    "7.decembris" : -8,
}

datums = input("Ievadiet datumu (piemēram, '1.decembris'): ")
if datums in gradi.keys(): #Pārbauda vai atslēga ir vārdnīcā.
    gradi_faren = gradi[datums] * 9/5 + 32 #Izrēķina Fārenheita grādus pēc Celsija grādiem ar formulu °F = C° * (9/5) + 32.

    print(f"{datums} temperatūra Celsija skalā ir: {gradi[datums]} grādi")
    print("*****")
    print(f"{datums} temperatūra Fārenheita skalā ir: {gradi_faren} grādi")

else: #Ja nav pareiza atslēga.
    for i in range(3): #For cikls dod vēl 3 mēģinājumus.
        print("Nepareiza atslēga. Lūdzu, ievadiet datumu no 1. līdz 7.decembrim.")

        datums = input("Ievadiet datumu (piemēram, '1.decembris'): ")
        if datums in gradi.keys(): #Pārbauda vai atslēga ir vārdnīcā.
            gradi_faren = gradi[datums] * 9/5 + 32 #Izrēķina Fārenheita grādus pēc Celsija grādiem ar formulu °F = C° * (9/5) + 32.

            print(f"{datums} temperatūra Celsija skalā ir: {gradi[datums]} grādi")
            print("*****")
            print(f"{datums} temperatūra Fārenheita skalā ir: {gradi_faren} grādi")
            break #Ja ir pareizi tad iziet no for cikla un beidzas programma.