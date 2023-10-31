name = "skolotaja"  #parole un lietotājvārds
password = "12345"

def numbers(a, b):  #funkcija izrēķina secīgi piegošu skaitļu summu
    sum = 0
    if a > b:
        return 0
    for i in range(a, b):
        sum += i
    sum += b
    return sum

for i in range(6):  #iet cauri programmai sešas reizes lai būtu 5 mēģinājumi pēc nepareizi ievadītas paroles vai lietotājvārda
    name_input = input("Lūdzu, ievadiet savu lietotājvārdu: ")
    if name_input == "stop" or name_input == "iziet":
        print("Programmas beigas!")
        break
    password_input = input("Lūdzu, ievadiet savu paroli: ")
    if password_input == "stop" or password_input == "iziet":
        print("Programmas beigas!")
        break
        
    if name_input == name and password_input == password:   #pareiza parole un pareizs lietotājvārds
        print("Pieslēgšanās veiksmīga")
        num1 = input("Ievadiet 1. veselo skaitli: ")
        if num1 == "stop" or num1 == "iziet":
            print("Programmas beigas!")
            break
        num2 = input("Ievadiet 2. veselo skaitli: ")
        if num2 == "stop" or num2 == "iziet":
            print("Programmas beigas!")
            break

        num1 = int(num1)    #pārveido ievadītos skaitļus uz int
        num2 = int(num2)
        sum = numbers(num1, num2)   #izrēķina secīgi pieaugošu skaitļu summu
        if num1 > 0 and num2 > 0:
            print(f"Veselu secīgi pieaugošu  skaitļu no {num1} līdz {num2} summa ir {sum}", end=" ")
        else:
            print("Nedrīkst būt negatīvs skaitlis!")
        if num1 > num2 and num1 >= 0 and num2 >= 0:
            print("jo 2. skaitlis ir mazāks kā pirmais!")
        break

    elif len(password_input) != 5: #ja parole nav piecas rakstzīmes gara
        print("Parolei jābūt 5 rakstzīmes garai!")
    elif password_input != password or name_input != name: #ja ir nepareizs lietotājvārds vai parole
        print("Nepareizs lietotājvārds vai parole")
    if i != 5:
        print(f"Ir atlikuši vēl {5-i} mēģinājumi!")
    else:
        print("Atļauts mēģināt pieslēgties 5 reizes!")
