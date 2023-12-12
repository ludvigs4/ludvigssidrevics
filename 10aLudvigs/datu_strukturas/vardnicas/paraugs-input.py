#izveidot tukšu vārdnīcu
vardnica = {
    "a" : 69
}

ievade_atslega = input("Ievadiet atslēgu: ")
ievade_vertiba = input("Ievadiet vērtību: ")

#pārauda lietotāja ievadi un rediģē vārdnīcu
if ievade_atslega in vardnica:
    vardnica[ievade_atslega] = ievade_vertiba
    print("Vārdnīca tika atjaunināta")
else:
    vardnica[ievade_atslega] = ievade_vertiba
    print("Jauns pāris tika pievienots vārdnīcai")

print(f"atjaunotā vārdnīca: {vardnica}")
