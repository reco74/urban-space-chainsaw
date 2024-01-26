def text_adventure_game():
    print("Willkommen zum Text Adventure Game!")
    print("Du stehst vor in einem dunklen Wald und hast drei Wege vor dir.")
    
    
    print("1. Gehe den linken Weg.")
    print("2. Gehe den rechten Weg.")
    print("3. Beende das Abenteuer.")

    wahl = input("Welchen Weg wählst du? (1/2/3): ")
    print("")

    while True:
          
        if wahl == "1":
            print("")
            print("Du folgst dem linken Weg und triffst auf einen freundlichen Kobold.")
            print("Du hast folgende Optionen:")
            print("1. Du greifst den Golem an")
            print("2. Du sprichst den Golem an")
            wahl2 = input("Welche Option wählst du? (1/2): ")
            print("")

            
            if wahl2 == "1":
                print("Der Golem ist stärker und tötet dich. Du hast verloren")
                break
            elif wahl2 == "2":
                print("Der Golem scheint nett zu sein. Er führt dich aus dem dunklen Wald raus. Du gewinntst!")
                break
            else:
                print("Ungürlige Eigabe. Bitte wähle 1 oder 2")
                break

        elif wahl == "2":
            print("Du gehst den rechten Weg und stolperst über eine verborgene Fallgrube.")
            print("Du stirbst und verlierst")
            break

        elif wahl == "3":
            print("Du entscheidest, das Abenteuer zu beenden. Bis zum nächsten Mal!")
            break

        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")
            break


text_adventure_game()