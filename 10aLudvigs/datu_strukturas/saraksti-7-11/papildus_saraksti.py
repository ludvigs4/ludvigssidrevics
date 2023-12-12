#piemērs sarakstam ar dažādiem datu tipiem
mixed_list = ["suns", 3, 1.5, True]
print(mixed_list[2])

skaitli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 69, 420, 22, 10, 12]
apgriezts = list(reversed(skaitli))
print(apgriezts)

para_skaitli = [num for num in skaitli if num %2 == 0]
print(para_skaitli)

videjais = sum(skaitli) / len(skaitli)
print(f"Vidējais sarakstam ir {videjais}")

#atrast lielāko un mazāko skaitli
liels = max(skaitli)
mazs = min(skaitli)
print(f"lielākais skaitlis {liels}")
print(f"Mazākais skaitlis: {mazs}")

augli = ["mango", "ābols", "apelsīns", "bumbieris", "citrons"]
#atrast vārdas, kas sākas ar konkrētu burtu
burts = [vards for vards in augli if vards.startswith("a")]
print(f"Vārdi, kas sākas ar a: {burts}")