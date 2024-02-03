import pygame

# Pygame initialisieren
pygame.init()

# Bildschirm erstellen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame mit Pfeiltasten")

# Spieler erstellen
spieler_breite, spieler_höhe = 50, 50
player_x, player_y = (width - spieler_breite) // 2, (height - spieler_höhe) // 2
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
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Bildschirm löschen
    screen.fill((255, 255, 255))

    # Spieler zeichnen
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, spieler_höhe, spieler_breite))

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Begrenzung der Aktualisierungsfrequenz
    clock.tick(60)

# Pygame beenden
pygame.quit()