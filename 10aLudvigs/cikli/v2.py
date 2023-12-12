# atbilde = "j"
# while atbilde == "j":
#     print("Nekusties!")
#     atbilde = input("Vai briesmonis draudzīgs?")
# print("Bēdz prom")

# pārbaudīt vai lietotājs prot reizrēķinu līdz 7
skaitlis = int(input("Ar ko jūs gribat saukt reizrēķinu?"))
for i in range(1, 13):
    print("Cik ir", i, "*", skaitlis, ":", end="")
    inpt = input()

    if inpt == "stop":
        break
    elif inpt == "nez":
        continue
    
    int_inp = int(inpt)
    if int_inp == i * skaitlis:
        print("Pareizi!")
    elif int_inp != i * skaitlis:
        print("Nepareizi!")
        print("atbilde ir:", i * skaitlis)
        break