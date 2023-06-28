import pygame
from assets.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/images/spaceship.png")
        self.image = pygame.transform.scale(self.original_image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = 640
        self.rect.bottom = 720
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Ensure the player stays within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        bullets.add(bullet)