
def filtere_tiere_nach_anfangsbuchstaben(tiere, anfangsbuchstabe):
    return [tier for tier in tiere if tier.startswith(anfangsbuchstabe)]


tiere_liste = ["Hund", "Katze", "Elefant", "Pinguin", "Giraffe"]

anfangsbuchstabe = input("Gib den Anfangsbuchstaben ein: ")


ausgewaehlte_tiere = filtere_tiere_nach_anfangsbuchstaben(tiere_liste, anfangsbuchstabe)
print(f"Die Tiere, deren Namen mit '{anfangsbuchstabe}' beginnen, sind: {ausgewaehlte_tiere}")