
def berechne_faktorial(zahl):
    if zahl == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1, zahl + 1):
            faktorial = faktorial * i
        return faktorial

print("Gib eine Zahl an: ")

zahl = int(input(""))
ergebnis = berechne_faktorial(zahl)
print(f'Der Faktorial von {zahl} ist {ergebnis}')