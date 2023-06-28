import pygame
import random
from assets.player import Player
from assets.enemy import Enemy
from assets.bullet import Bullet


pygame.init()
screen = pygame.display.set_mode((800, 720))
pygame.display.set_caption("Space Invaders")

# Create player and bullet groups

player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create enemies
enemy = Enemy(100, 100)
enemies.add(enemy)

# Game loop

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(bullets)

    screen.fill((0, 0, 0))  # Fill the screen with black
    player.update()  # Update the player's position
    enemies.update()  # Update the player's position
    bullets.update()  # Update the player's position
    player.draw(screen)  # Draw the player on the screen
    enemies.draw(screen)  # Draw the player on the screen
    bullets.draw(screen)  # Draw the player on the screen

    pygame.display.flip()
    clock.tick(60)

pygame.quit()