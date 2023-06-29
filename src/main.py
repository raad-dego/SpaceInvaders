import pygame
import random
from player import Player
from enemy import Enemy
from game import Scoreboard

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Create player, bullets, and scoreboard
player = Player(screen_width, screen_height)
bullets = pygame.sprite.Group()
scoreboard = Scoreboard()

# Create enemies
enemies = pygame.sprite.Group()
destroyed_enemies = 0
enemy_spawn_interval = 1000
enemy_spawn_timer = pygame.time.get_ticks() + enemy_spawn_interval

# Game over variables
game_over = False
game_over_text = pygame.font.Font(None, 64).render("Game Over", True, (255, 255, 255))
game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
score_text = pygame.font.Font(None, 32).render("Score: 0", True, (255, 255, 255))
score_text_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot(bullets)
            elif event.key == pygame.K_RETURN and game_over:
                # Reset the game state to play again
                enemies.empty()
                bullets.empty()
                destroyed_enemies = 0
                enemy_spawn_interval = 1000
                enemy_spawn_timer = pygame.time.get_ticks() + enemy_spawn_interval
                player.reset(screen_width, screen_height)
                scoreboard.reset()
                game_over = False

    if not game_over:
        # Update game objects
        player.update()
        enemies.update()
        bullets.update()

        current_time = pygame.time.get_ticks()

        # Spawn enemies at random intervals
        if current_time >= enemy_spawn_timer:
            x = random.randint(0, screen_width - 50)
            y = random.randint(-100, -50)
            enemy = Enemy(screen_width, screen_height)
            enemies.add(enemy)

            # Decrease the spawn interval by 50 milliseconds for every 10 destroyed enemies
            if destroyed_enemies % 10 == 0:
                enemy_spawn_interval -= 50

            enemy_spawn_timer = current_time + enemy_spawn_interval

        # Collision detection
        player_hit = pygame.sprite.spritecollideany(player, enemies, pygame.sprite.collide_mask)
        if player_hit:
            game_over = True

    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollideany(bullet, enemies, pygame.sprite.collide_mask)
        if enemy_hit:
            bullets.remove(bullet)  # Remove the bullet if it hits an enemy
            enemies.remove(enemy_hit)  # Remove the enemy from the group
            destroyed_enemies += 1
            scoreboard.increase_score()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    screen.fill((0, 0, 0))  # Fill the screen with black

    bullets.draw(screen)
    enemies.draw(screen)
    player.draw(screen)
    scoreboard.draw(screen)

    if game_over:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(score_text, score_text_rect)
        score_text = pygame.font.Font(None, 32).render(f"Score: {scoreboard.score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(score_text, score_text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
