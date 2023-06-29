import pygame

import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load("assets/images/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -screen_height
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        # Check if the enemy has reached the bottom of the screen
        if self.rect.y > pygame.display.get_surface().get_height():
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
