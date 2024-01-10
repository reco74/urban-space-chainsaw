def wechselkurs(betrag, wechsel):
    return betrag * wechsel

waehrung = input("Währung (USD oder EUR): ")
betrag = float(input("Betrag: "))

if waehrung == "USD":
    ergebnis = wechselkurs(betrag, 0.9)
    print(f'{betrag} USD sind {ergebnis} EUR')
if waehrung == "EUR":
    ergebnis = wechselkurs(betrag, 1.1)
    print(f'{betrag} EUR sind {ergebnis} USD')
else:
    print("Währung nicht unterstützt")