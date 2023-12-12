age = float(input("Ievadiet suņa vecumu:"))

if age <= 2:
    print("Jūsu suns ir", age * 10.5, "gadus vecs suņa gados")
else:
    print("Jūsu suns ir", (age - 2) * 4 + 21, "gadus vecs suņa gados")