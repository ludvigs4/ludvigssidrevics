gads = int(input("Ievadi gadu: ")) #Lietotājs ievada gadu, kuam grib uzzināt gada garumu.

if gads % 4 == 0: #Izrēķina vai gads dalās ar 4 un nav atlikuma.
    print(f"{gads} ir garais gads.")
else: #Gads nedalās ar 4.
    print(f"{gads} ir īsais gads.")