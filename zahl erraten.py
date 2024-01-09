import random

x = random.randint(1,100)
print('Ich habe mir eine Zahl von 1-100 ausgedacht.')

while True:
    versuch = int(input('Rate meine Zahl: '))
    if versuch == x:
      print('Richtig erraten')
      break
    if versuch < x: print('zu klein!')
    if versuch > x: print('zu groß!')
