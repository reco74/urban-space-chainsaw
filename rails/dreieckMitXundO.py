zahls = input("Wie gross soll deine Zeile sein? " )

try:
        zahl = int(zahls)
except ValueError:
        print("Gib eine richtige Zahl ein")


def print_triangle():
      try:
            zahl = int(zahls)
      except ValueError:
            print("Gib eine richtige Zahl ein")

      for i in range(1, zahl + 1):
            left_side = 'x' * i
            right_side = 'o' * i
            spaces = ' ' * (zahl - i)
            print(f"{left_side}{spaces}  {right_side.rjust(zahl * 2)}")

       for i in range(zahl - 1, 0, -1):
            left_side = 'x' * i
            right_side = 'o' * i
            spaces = ' ' * (zahl - i)
            print(f"{left_side}{spaces}  {right_side.rjust(zahl * 2)}")

    
    print_triangle()
