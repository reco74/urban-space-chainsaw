name = input("Wie lautet dein Name? ")

try:
    alter = int(input("Wie alt bist du? "))
except ValueError:
    print("Bitte gib eine gültige Zahl für dein Alter ein.")
    exit()

if alter < 18:
    print(f"Hallo {name}! Du bist noch minderjährig.")
elif 18 <= alter < 65:
    print(f"Hallo {name}! Willkommen im Erwachsenenalter.")
else:
    print(f"Hallo {name}! Genieße deine Zeit im Seniorenalter.")