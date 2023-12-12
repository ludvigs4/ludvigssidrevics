skaitlis1 = int(input("Ievadiet pirmo skaitli!:"))
skaitlis2 = int(input("Ievadiet otro skaitli!:"))

if skaitlis1 >= 8 and skaitlis1 <= 25:
    if skaitlis2 >= 8 and skaitlis2 <= 25:
        print("Paldies, skaitļi ievadīti kā prasīts!")
    if skaitlis2 < 8 or skaitlis2 > 25:
        print("Viens skaitlis nav pareizs!")

elif skaitlis2 >= 8 and skaitlis2 <= 25:
    if skaitlis1 >= 8 and skaitlis1 <= 25:
        print("Paldies, skaitļi ievadīti kā prasīts!")
    if skaitlis1 < 8 or skaitlis1 > 25:
        print("Viens skaitlis nav pareizs!")

else:
    print("Jālasa noteikumi vēlreiz!")