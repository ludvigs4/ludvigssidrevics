import math

cukurs_cena = 1.3
citrons_cena = 0.86
kanelis_cena = 0.39

print("Ievadiet recepti uz litru ievārījuma!")
abols_daudzums = float(input("Cik kg abolu tev vajag?"))
udens_daudzums = float(input("Cik litru ūdens vajadzēs?"))
cukurs_daudzums = float(input("Cik kg cukuru vajag?"))
citrons_daudzums = int(input("Cik citronus tev vajag?"))
kanelis_daudzums = float(input("Cik g kanēļa vajag?"))


abols_raza = float(input("Cik tev kg ābolu?"))
print(f"Jūs varat izvārīt {round(abols_raza/abols_daudzums, 1)}l ievārījuma!")

cukurs_majas = float(input("Cik tev kg cukura ir mājās?"))
citrons_majas = float(input("Cik tev citroni mājās?"))
kanelis_majas = float(input("Cik tev g kanēļa ir mājās?"))

cukurs_cena = float(input("Cik maksā cukurs(1 kg)?"))
citrons_cena = float(input("Cik maksā citrons(1 gab.)?"))
kanelis_cena = float(input("Cik maksā kanēlis(15g)?"))

litri = round(abols_raza / abols_daudzums, 1)

cukurs_summa = math.ceil(cukurs_daudzums - cukurs_majas) * cukurs_cena
citrons_summa = math.ceil(citrons_daudzums - citrons_majas) * citrons_cena
kanelis_summa = kanelis_cena * 

print("Cukurs maksā", cukurs_summa, "EUR")
print("Citrons maksā", citrons_summa, "EUR")
print("Kanelis maksā", kanelis_summa, "EUR")