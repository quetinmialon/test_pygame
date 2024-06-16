import pygame
from Player import Player
from monster import *
from comete_event import cometFallEvent
from sounds import SoundManager

class Game:
    def __init__(self):
        self.is_playing = False 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.comet_event = cometFallEvent(self)
        self.score = 0
        self.font = pygame.font.SysFont('gothica', 30)
        self.sound_manager = SoundManager()


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.player.update_animation()
        self.comet_event.update_bar(screen)
        
        for missile in self.player.all_missiles:
            missile.move()
            
        for monster in self.all_monsters: 
            monster.move()
            monster.update_health_bar(screen)
            monster.update_animation()
            
        for comet in self.comet_event.all_commets:
            comet.fall()
            
        self.player.all_missiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_event.all_commets.draw(screen)
        
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
            
        
        score_text = self.font.render(f'score : {self.score}',1, (250,250,250))
        screen.blit(score_text, (20,20))

    def game_over(self):
        self.all_monsters.empty()
        self.comet_event.all_commets.empty()
        self.player.health = self.player.max_health
        self.comet_event.reset()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def start(self):
        self.is_playing = True
        self.all_monsters.empty()  
        self.comet_event.reset()  
        for i in range(2):
            self.spawn_monster(Mummy)   
        self.spawn_monster(Alien)

    def spawn_monster(self, monster_class):
        self.all_monsters.add(monster_class(self))
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
