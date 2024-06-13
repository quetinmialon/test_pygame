import pygame
from Player import Player
from monster import Monster
from comete_event import cometFallEvent
import random

class Game : 
    def __init__(self):
        self.is_playing = False 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.comet_event = cometFallEvent(self)

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)


        for missile in self.player.all_missiles:
            missile.move()
        

        for monster in self.all_monsters : 
            monster.move()
            monster.update_health_bar(screen)

        for comet in self.comet_event.all_commets :
            comet.fall()
            
        self.player.all_missiles.draw(screen)

        self.all_monsters.draw(screen)

        self.comet_event.all_commets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def game_over (self): 
      self.all_monsters = pygame.sprite.Group()
      self.player.health = self.player.max_health
      self.is_playing = False
    
    def start(self):
        self.is_playing = True
        i = random.randint(1, 4)
        for x in range(i) :
            self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask)

