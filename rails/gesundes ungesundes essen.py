gesund = ['Apfel', 'Banane', 'Birne']
ungesund = ['Burger', 'Pizza', 'Pommes']
eingabe = input('Willst du eine gesunde oder ungesunde Auswahl an essen?: \n')


if eingabe == "gesund":
    print("Gesundes Essen: \n")
    for i in gesund:
        print(i)
if eingabe == "ungesund":
    print("Ungesundes Essen: \n")
    for i in ungesund:
        print(i)
