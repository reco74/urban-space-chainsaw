import random

def kopf_oder_zahl():
    ergebnis = random.choice(['Kopf', 'Zahl'])
    return ergebnis


ergebnis = kopf_oder_zahl()
print(f'Das Ergebnis ist: {ergebnis}')