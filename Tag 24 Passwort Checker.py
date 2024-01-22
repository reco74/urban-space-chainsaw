def passwort_checker(passwort):
   
    if len(passwort) < 8:
        return "Das Passwort ist zu kurz. Es muss mindestens 8 Zeichen lang sein."

    if not any(p.isupper() for p in passwort):
        return "Das Passwort muss mindestens einen Großbuchstaben enthalten."

    if not any(p.islower() for p in passwort):
        return "Das Passwort muss mindestens einen Kleinbuchstaben enthalten."

    return "Das Passwort ist gültig."


benutzer_passwort = input("Geben Sie Ihr Passwort ein: ")
ergebnis = passwort_checker(benutzer_passwort)
print(ergebnis)