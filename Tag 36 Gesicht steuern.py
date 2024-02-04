import pygame

# Pygame initialisieren
pygame.init()

# Bildschirm erstellen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame mit Pfeiltasten")

# Spieler erstellen
spieler_radius = 25
spieler_x, spieler_y = (width - spieler_radius) / 2, (height - spieler_radius) / 2
player_speed = 5

# Pygame Schleife
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        spieler_y -= player_speed
    if keys[pygame.K_DOWN]:
        spieler_y += player_speed
    if keys[pygame.K_LEFT]:
        spieler_x -= player_speed
    if keys[pygame.K_RIGHT]:
        spieler_x += player_speed

    # Bildschirm löschen
    screen.fill((255, 255, 255))

    # Spieler zeichnen (Kreis für Kopf, Rechteck für Körper und Beine)
    pygame.draw.circle(screen, (0, 0, 255), (spieler_x + spieler_radius, spieler_y + spieler_radius), spieler_radius)
    pygame.draw.circle(screen, (0, 200, 255), (spieler_x + 15, spieler_y + 15), spieler_radius - 20)
    pygame.draw.circle(screen, (0, 200, 255), (spieler_x + 35, spieler_y + 15), spieler_radius - 20)
    pygame.draw.rect(screen, (0, 200, 255), pygame.Rect(spieler_x + 13, spieler_y + 28, 25, 10))

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Begrenzung der Aktualisierungsfrequenz
    clock.tick(60)

# Pygame beenden
pygame.quit()