def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ungültige Eingabe. Division durch Null ist nicht erlaubt."

print("Einfacher Taschenrechner")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

choice = input("Wählen Sie eine Operation (1/2/3/4): ")

num1 = float(input("Geben Sie die erste Zahl ein: "))
num2 = float(input("Geben Sie die zweite Zahl ein: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Ungültige Eingabe. Bitte wählen Sie eine gültige Operation.")
