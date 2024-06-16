import pygame
import random
import animation
class Monster (animation.AnimateSprite): 
    def __init__(self, game, name, size, offset = 0, score = 100):

        
        super().__init__(name, size)

        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 500 + random.randint(0,100) - offset
        self.start_animation()
        self.score = score

    def update_health_bar(self, surface):
      
        pygame.draw.rect(surface,(80,80,80),[self.rect.x + 10,self.rect.y-20,self.max_health,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10,self.rect.y-20,self.health,5])

    def update_animation(self):
        self.animate(True)
    
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1,self.default_speed)
    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()
                
            else:
                self.rect.x = 1000 + random.randint(0, 300)
                self.health = self.max_health
                self.velocity = random.randint(1, 3)
            self.game.score += self.score

    def move(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else :
            self.game.player.damage(self.attack)


class Mummy (Monster):
    def __init__(self, game):
        self.set_speed(4)
        super().__init__(game, "mummy",(130,130))
        self.attack = 0.8
        
class Alien (Monster):
    def __init__(self, game):
        self.set_speed(2)
        super().__init__(game, "alien",(300,300), 150, 500)
        self.health = 250
        self.max_health = 250
        self.attack = 1.5