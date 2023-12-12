saraksts = [1, 2, 3 , 4, 5]
saraksts.append("cepums")#pievieno beigās
print(saraksts)

saraksts.pop()
print(saraksts)

saraksts.insert(3, "Hello")#ieieto 3. elementu
print(saraksts)

saraksts.remove(4)#izdzēš norādīto vērtību
print(saraksts)

tests = [1, 2, 3, 4, 5, 6, 7, 8]
del tests[2] #izdzēš saraksta indeksa vērību
print(tests)

del tests[3:6]#izdzēš intervālu
print(tests)

cipari = [1, 2, 3, 4, 5, 6, 7, 8]
del cipari[2:5:2]#2-7 elementa dzēš katru otro elementu
print(cipari)