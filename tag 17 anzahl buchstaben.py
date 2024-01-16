
def zaehle_buchstaben(wort):
    return len(wort)

# Benutzereingabe für das Wort
eingabe = input("Gib ein Wort ein: ")

# Zählung der Buchstaben und Ausgabe des Ergebnisses
anzahl_buchstaben = zaehle_buchstaben(eingabe)
print(f"Das eingegebene Wort hat {anzahl_buchstaben} Buchstaben.")