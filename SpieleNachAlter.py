print('Spieleangebote für dich')

spiele0 = ['Fall guys', 'Monopoly', 'Sonic The Hedgehog']

spiele6 = ['Minecraft', 'Sackboy', 'Lego Worlds']

spiele12 = ['Gang Beasts', 'Spider Man', 'Fortnite']

spiele16 = ['Battlefield', 'Modern Warfare 2', 'Rainbow Six']

spiele18 = ['GTA 5', 'Red Dead Redemption', 'God of War']


alter = int(input("Wie alt bist du?: "))

if alter < 6:
    print("Spiele unter 6 Jahren: \n")
    for i in spiele0:
        print(i)

elif alter < 12:
    print("Spiele unter 12 Jahren: \n")
    for i in spiele0:
        print(i)
    for b in spiele6:
        print(b)

elif alter < 16:
    print("Spiele unter 16 Jahren: \n")
    for i in spiele0:
        print(i)
    for b in spiele6:
        print(b)
    for a in spiele12:
        print(a)

elif alter < 18:
    print("Spiele unter 18 Jahren: \n")
    for i in spiele0:
        print(i)
    for b in spiele6:
        print(b)
    for a in spiele12:
        print(a)
    for n in spiele16:
        print(n)

elif alter >= 18:
    print("Spiele unter und ab 18 Jahren: \n")
    for i in spiele0:
        print(i)
    for b in spiele6:
        print(b)
    for a in spiele12:
        print(a)
    for n in spiele16:
        print(n)
    for k in spiele18:
        print(k)
