import pygame
import random

from monster import *

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,2)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event
    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 540:
            self.remove()
            if len(self.comet_event.all_commets) == 0:
                self.comet_event.reset()
                self.comet_event.fall_mode = False  
                self.comet_event.meteors_generated = False  

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)
            
        if len(self.comet_event.all_commets) == 0:
            self.comet_event.reset()
            self.comet_event.fall_mode = False 
            self.comet_event.meteors_generated = False  
            self.comet_event.game.start()

    def remove(self):
        self.comet_event.all_commets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
