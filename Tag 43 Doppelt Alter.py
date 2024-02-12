alter_liste = [20, 25, 30, 25, 35, 40, 30, 45, 25]


doppelte_alter = [item for item in set(alter_liste) if alter_liste.count(item) > 1]

if doppelte_alter:
    print("Doppelte Alter in der Liste:", doppelte_alter)
else:
    print("Es gibt keine doppelten Alter in der Liste.")