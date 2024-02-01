import pygame
import sys
import time

pygame.init()


# Farbeingabe im Terminal abfragen
farbeEingabe = input("Suchen Sie aus zwischen rot, blau und grün: ")

# Farben definieren
farbe = {'rot': (255, 0, 0), 'grün': (0, 255, 0), 'blau': (0, 0, 255)}

# Überprüfen, ob die eingegebene Farbe verfügbar ist
if farbeEingabe in farbe:

    width, height = 400, 300
    screen = pygame.display.set_mode((width, height))
    
    gewaehlteFarbe = farbe[farbeEingabe]

    # Bildschirm mit der ausgewählten Farbe füllen
    screen.fill(gewaehlteFarbe)
    pygame.display.flip()

    # Warte 3 Sekunden
    time.sleep(10)

else:
    print("Ungültige Farbe. Das Programm wird beendet.")
    pygame.quit()
    sys.exit()

# Pygame beenden
pygame.quit()
sys.exit()