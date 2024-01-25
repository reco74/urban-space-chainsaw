import random

def satz_generator():
    adjektive = ["rote", "lustige", "schnelle", "interessante", "klebrige", "große"]
    substantiven = ["Hund", "Löwe", "Elefant", "Boxer", "Computer"]
    verben = ["springt", "tanzt", "schlürft", "lächelt", "wackelt"]

    zufaelliges_adjektiv = random.choice(adjektive)
    zufaelliges_substantiv = random.choice(substantiven)
    zufaelliges_verb = random.choice(verben)

    print(f"Der {zufaelliges_adjektiv} {zufaelliges_substantiv} {zufaelliges_verb}.")

    

satz_generator()