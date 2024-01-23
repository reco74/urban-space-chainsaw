def nummer(a):   
     
    if isinstance(a, (int, float)):
        if a > 0:   
            print("Die Nummer ist positiv")   
     
        elif a < 0:   
            print("Die Nummer ist negativ")   
     
        else:   
            print("Die Nummer ist null")
    else:
        print("Fehler: Gib eine Zahl ein")  

try: 
    a = int(input("Nenn eine Zahl: "))  
    nummer(a)
except ValueError:
    print("Fehler: Gib eine Zahl ein")
