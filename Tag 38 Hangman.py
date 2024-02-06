import random

def wähle_wort():
    wortliste = ["python", "hangman", "programmierung", "computer", "wissenschaft", "algorithmus"]
    return random.choice(wortliste)

def zeige_wort(wort, geratene_buchstaben):
    anzeige = ""
    for buchstabe in wort:
        if buchstabe in geratene_buchstaben:
            anzeige += buchstabe
        else:
            anzeige += "_"
    return anzeige

def hangman():
    print("Willkommen beim Hangman-Spiel!")

    # Wähle ein zufälliges Wort
    geheimes_wort = wähle_wort()

    # Initialisiere Variablen
    geratene_buchstaben = []

    while True:
        # Zeige den aktuellen Wortzustand an
        aktuelle_anzeige = zeige_wort(geheimes_wort, geratene_buchstaben)
        print("Aktuelles Wort:", aktuelle_anzeige)

        # Überprüfe, ob das Spiel gewonnen wurde
        if "_" not in zeige_wort(geheimes_wort, geratene_buchstaben):
            print("Herzlichen Glückwunsch! Du hast das Wort erraten:", geheimes_wort)
            break

        # Eingabe des Spielers
        eingabe = input("Rate einen Buchstaben: ").lower()

        # Überprüfe, ob der Buchstabe bereits geraten wurde
        if eingabe in geratene_buchstaben:
            print("Du hast diesen Buchstaben bereits geraten. Versuche es erneut.")
            continue

        # Füge den geratenen Buchstaben zur Liste der geratenen Buchstaben hinzu
        geratene_buchstaben.append(eingabe)

        # Überprüfe, ob der geratene Buchstabe im Wort ist
        if eingabe not in geheimes_wort:
            print("Falsch! Versuche es weiter.")

# Starte das Hangman-Spiel
hangman()