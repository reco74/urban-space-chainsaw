def filtere_auto_nach_anfangsbuchstaben(automarken_liste, anfangsbuchstabe):
    return [marke for marke in automarken_liste if marke.startswith(anfangsbuchstabe)]

automarken_liste = ["Volkswagen", "Toyota", "Ford", "BMW", "Mercedes-Benz", "Honda", "Chevrolet", "Audi", "Nissan", "Tesla"]

anfangsbuchstabe = input("Gib den Anfangsbuchstaben ein: ")

gefilterte_marken = filtere_auto_nach_anfangsbuchstaben(automarken_liste, anfangsbuchstabe)
print(f"Die Automarken, deren Namen mit '{anfangsbuchstabe}' beginnen, sind: {gefilterte_marken}")