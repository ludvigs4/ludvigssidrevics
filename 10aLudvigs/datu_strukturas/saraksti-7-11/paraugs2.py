krasas = ["zils", "melns", "sarkans", "zaļš"]
jauns = []
for i in krasas:
    burti = 0
    for j in i:
        burti += 1
    pagaidu_saraksts = [i, burti]
    jauns.append(pagaidu_saraksts)
print(jauns)

for i in krasas:
    print(i, len(i))