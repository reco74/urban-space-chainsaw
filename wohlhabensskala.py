print('Wohlhaben Skala')

while True:
    einkommen = int(input("Was ist dein Monatseinkommen?: "))
    if einkommen < 50: print('broker als ich')
    elif einkommen < 100: print('No money brother')
    elif einkommen < 2000: print('unterdurchschnittlich')
    elif einkommen < 3800: print('durchschnitt bruderherz')
    elif einkommen < 6000: print('überdurchschnittlich habibi')
    elif einkommen < 12000: print('mies para')
    elif einkommen < 100000: print('übertrieben wohlhabend')
    elif einkommen >= 100000: print('übetrieben reicher habibi')
