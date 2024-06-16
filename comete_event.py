import pygame
from comete import Comet

class cometFallEvent:
    def __init__(self, game):
        self.game = game
        self.reset()

    def reset(self):
        self.percent = 0
        self.percent_speed = 15
        self.all_commets = pygame.sprite.Group()
        self.fall_mode = False
        self.meteors_generated = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def update_bar(self, surface):
        self.add_percent()
        self.attempt_fall()
        pygame.draw.rect(surface, (40, 40, 40), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (255, 40, 40), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])

    def meteor_fall(self):
        print("Déclenchement de la chute des météores.")
        for i in range(20):
            self.all_commets.add(Comet(self))

    def is_full_loaded(self):
        return self.percent >= 100

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0 and not self.fall_mode and not self.meteors_generated:
            self.meteor_fall()
            self.meteors_generated = True
            self.fall_mode = True
