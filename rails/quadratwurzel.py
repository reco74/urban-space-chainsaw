import math


zahl = input("Gib eine Zahl ein:" )

try:
    zahl2 = float(zahl)
except ValueError:
    print("Ungültige Zahl")
    exit()

wurzel = math.sqrt(zahl2)

print(f"Die Wurzel deiner Zahl ist {wurzel}")
