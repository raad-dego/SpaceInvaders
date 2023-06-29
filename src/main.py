import pygame
import random
from player import Player
from enemy import Enemy

pygame.init()
screen_width = 800  # Set the desired width of the window
screen_height = 600  # Set the desired height of the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Create player and enemy groups
player = Player(screen_width, screen_height)
bullets = pygame.sprite.Group()

# Create enemies
enemies = pygame.sprite.Group()
destroyed_enemies = 0  # Number of destroyed enemies
enemy_spawn_interval = 2000  # Initial interval for enemy spawns (in milliseconds)
enemy_spawn_timer = pygame.time.get_ticks() + enemy_spawn_interval

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

    current_time = pygame.time.get_ticks()

    # Spawn enemies at random intervals
    if current_time >= enemy_spawn_timer:
        x = random.randint(0, screen_width - 50)  # Random x-coordinate
        y = random.randint(-100, -50)  # Random y-coordinate above the screen
        enemy = Enemy(screen_width, screen_height)
        enemies.add(enemy)

        # Decrease the spawn interval by 50 milliseconds for every 10 destroyed enemies
        if destroyed_enemies % 10 == 0:
            enemy_spawn_interval -= 50

        # Set the timer for the next enemy spawn
        enemy_spawn_timer = current_time + enemy_spawn_interval

    # Collision detection
    player_hit = pygame.sprite.spritecollide(player, enemies, False)
    if player_hit:
        running = False  # End the game if the player collides with an enemy

    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemy_hit:
            bullets.remove(bullet)  # Remove the bullet if it hits an enemy
            destroyed_enemies += 1

    screen.fill((0, 0, 0))  # Fill the screen with black

    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
