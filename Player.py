import pygame
from Missile import Missile
import animation

class Player(animation.AnimateSprite): 
    def __init__(self, Game):
        super().__init__('player')
        self.game = Game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_missiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.y = 500
        self.rect.x = 0
    
    def move_right(self):

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def launch_missile(self):
        self.all_missiles.add(Missile(self))
        self.start_animation()
        self.game.sound_manager.play('tir')
    
    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
      
        pygame.draw.rect(surface,(80,80,80),[self.rect.x +50,self.rect.y+20,self.max_health,7])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x +50,self.rect.y+20,self.health,7])

    def damage(self, damage):
        if self.health - damage > damage :
            self.health -= damage
        else : 
            self.game.game_over()
