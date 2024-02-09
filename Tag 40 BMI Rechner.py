def bmi_rechner(gewicht, groesse):
    bmi = gewicht / (groesse ** 2)
    return bmi

def bmi_bewertung(bmi):
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 25:
        return "Normalgewicht"
    elif 25 <= bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

# Benutzereingabe
gewicht = float(input("Gib dein Gewicht in Kilogramm ein: "))
groesse = float(input("Gib deine Größe in Metern ein: "))

# BMI berechnen
bmi = bmi_rechner(gewicht, groesse)

# BMI bewerten
bewertung = bmi_bewertung(bmi)

# Ergebnis ausgeben
print(f"Dein BMI beträgt: {bmi:.2f}")
print(f"Bewertung: {bewertung}")