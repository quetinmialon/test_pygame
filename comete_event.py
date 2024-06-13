import pygame
from comete import Comet

class cometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 50
        self.all_commets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    
    def update_bar(self, surface):

        self.add_percent()
        self.attempt_fall()
        self.fall_mode = True
        pygame.draw.rect(surface, (40,40,40),[0,surface.get_height()-20,surface.get_width(),10])
        pygame.draw.rect(surface, (255,40,40),[0,surface.get_height()-20,(surface.get_width()/100)*self.percent,10])
        
    def meteor_fall(self):
        self.all_commets.add(Comet(self))

    def is_full_loaded(self):
        return self.percent >= 100
    def reset_bar(self):
        self.percent = 0

    def attempt_fall(self):
        if self.is_full_loaded():
            self.meteor_fall()
            self.reset_bar()