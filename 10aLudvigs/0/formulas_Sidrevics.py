import math
import random

pi = 3.1415

rl = float(input("Ievadiet riņķa līnijas rādiusu:"))
print(rl)

print('Riņķā līnijas garums:',round(2*pi*rl, 2))
print('Riņķa līnijas laukums:',round(pi*pow(rl,2)))


katete1 = float(input('Ievadiet tiasnleņķa trijstūra pirmās katetes garumu:'))
katete2 = float(input('Ievadiet tiasnleņķa trijstūra otrās katetes garumu:'))

print('taisnleņķa trijstūra hipotenūzas garums ir:',round(math.sqrt(pow(katete1, 2)+pow(katete2, 2)),2)) #izrēķina hipotenūzu
print('Gadījuma skaitlis no 0 - 1:', random.random())