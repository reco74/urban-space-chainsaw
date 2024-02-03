import pygame
import turtle

# Pygame initialisieren
pygame.init()

# Bildschirm erstellen
screen = turtle.Screen()
screen.title("Pygame mit Turtle")
screen.bgcolor("white")

# Turtle erstellen
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(2)

# Pygame Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Turtle bewegen
    player.forward(200)
    player.right(90)
    player.forward(200)
    player.right(90)
    player.forward(200)
    player.right(90)
    player.forward(400)
    player.left(90)
    player.forward(200)
    player.left(90)
    player.forward(200)
    player.left(90)
    player.forward(200)

    # Bildschirm aktualisieren
    screen.update()

# Pygame beenden
pygame.quit()