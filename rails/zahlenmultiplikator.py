print("Zahlenmultiplikator")

szahl = input("Gib die erste Zahl ein: ")
szahl2 = input("Gib die zweite Zahl ein: ")

try:
    zahl = int(szahl)
    zahl2 = int(szahl2)
except ValueError:
    print("Gib eine richtige Zahl ein")

ergebnis = zahl*zahl2

print("Das Produkt deiner zwei Zahlen ergibt: ", ergebnis)
