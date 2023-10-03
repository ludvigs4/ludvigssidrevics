type = input("grāmata vai žurnāls?:")
requested = input("vai šis ir pieprasītais izdevums?:")
allowed = input("vai jums ir kāds laikā neatdots izdevums?:")

if requested == "jā" and allowed == "nē":
    print("grāmata tiek izsniegta uz 2 dienām")#ja ir pieprasīta grāmata

if type == "grāmata" and allowed == "nē" and requested == "nē":
    student = input("vai jūs esat students?:")
    if student == "jā":
        print("grāmata tiek izsniegta uz 14 dienām")#ja ir students un grāmata
    else:
        print("grāmata tiek izsniegta uz 28 dienām")#ja ir personāls

if type == "žurnāls" and allowed == "nē" and requested == "nē":
    print("žurnāls tiek izsniegts uz 7 dienām")#ja ir žurnāls

if allowed == "jā":
    print("jums ir laikā nenodots izdevums un jums netiek izniegti izdevumi!")#nenodota grāmata
