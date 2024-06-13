import pygame
import random

class Monster (pygame.sprite.Sprite): 
    def __init__(self, game):

        
        super().__init__()

        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(4,12) / 6
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 500 + random.randint(0,100)

    def update_health_bar(self, surface):
      
        pygame.draw.rect(surface,(80,80,80),[self.rect.x + 10,self.rect.y-20,self.max_health,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10,self.rect.y-20,self.health,5])

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0 :
            self.rect.x = 1000 + random.randint(0,300)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

    def move(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else :
            self.game.player.damage(self.attack)


