import math
import random

skaitlis = 43.7
print("noapaļots uz leju:", math.floor(skaitlis))
print("noapaļots uz augšu:", math.ceil(skaitlis))

print(pow(skaitlis, 2))
print(math.pow(4, 6))

pakape = int(input("pakape:"))
print("skaitlis pakape ir:", math.pow(skaitlis, pakape))

print("kvadrātsakne:", math.sqrt(skaitlis))

x = 56765/9654
print("x:", x)
print("formatēts x: " "%.6f"%x)
print("formatēts x: " "{:.6f}".format(x))

cipars = random.random()
print("random:", cipars)

cipars2 = random.randint(0, 10)
print("randint:", cipars2)