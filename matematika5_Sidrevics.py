import math

print("Programmu izstrādāja: Ludvigs, Sidrevics")
print("Laukuma aprēķins ģeometriskām figūrām\n\t****")

malaA = float(input("Ievadiet malas A garumu:"))
print("malas A garums:", malaA)
print("\t****")

malaB = float(input("Ievadiet malas B garumu:"))
print("malas B garums:", malaB)
print("\t****")

augstums = float(input("Iievadiet augstumu:"))
print("Augstums:", augstums)

s_trijst = malaA * augstums / 2
print("Laukums trijstūrim:", s_trijst)

s_trap = (malaA + malaB) / 2 * augstums
print("Laukums trapecei:", s_trap)

s_paral = malaA * augstums
print("Laukums paralelogramam:", s_paral)

print("\t****\nPaldies!")