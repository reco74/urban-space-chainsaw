alters = input("Wie alt bist du? ")

try:

    alter = int(alters)
except ValueError:
    print("Gib ein richtiges alter an")

print("Du bist ", alter, " Jahre alt")
