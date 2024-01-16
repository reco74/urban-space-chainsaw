def aeltere_personen(personen, altersschwelle):
    return [name for name, alter in personen if alter > altersschwelle]


personen = [("Alice", 28), ("Bob", 35), ("Charlie", 21)]

altersschwelle = int(input("Gib die Altersschwelle ein: "))


aelter = aeltere_personen(personen, altersschwelle)
print(f"Die Personen, die älter als {altersschwelle} sind, sind: {aelter}")