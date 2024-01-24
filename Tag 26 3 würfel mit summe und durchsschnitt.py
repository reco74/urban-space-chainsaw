import random

def wurfeln():
    return random.randint(1, 6)

def wurfspiel():
    anzahl_wurfe = 3
    wurf_ergebnisse = []

    for i in range(anzahl_wurfe):
        wurf = wurfeln()
        wurf_ergebnisse.append(wurf)
        print(f"Du hast eine {wurf} gewürfelt!")

    summe = sum(wurf_ergebnisse)
    durchschnitt = summe / anzahl_wurfe

    print(f"\nGesamtsumme der Würfe: {summe}")
    print(f"Durchschnitt der Würfe: {durchschnitt}")

print("Willkommen!")
wurfspiel()