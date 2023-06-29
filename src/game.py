import pygame

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  # Font for the scoreboard
        self.score = 0

    def increase_score(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def reset(self):
        self.score = 0