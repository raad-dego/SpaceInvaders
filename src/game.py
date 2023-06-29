import pygame
from player import Player
from enemy import Enemy

pygame.init()
screen_width = 800  # Set the desired width of the window
screen_height = 600  # Set the desired height of the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Create player and enemy groups
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create enemies
enemy = Enemy(screen_width)
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

    # Update game objects
    player.update()
    enemies.update()
    bullets.update()

    # Collision detection
    player_hit = pygame.sprite.spritecollide(player, enemies, False)
    if player_hit:
        running = False  # End the game if the player collides with an enemy

    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemy_hit:
            bullets.remove(bullet)  # Remove the bullet if it hits an enemy

    screen.fill((0, 0, 0))  # Fill the screen with black

    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
