import pygame

class AnimateSprite(pygame.sprite.Sprite):
    
    def __init__(self, spriteName, size = (200,200)):
        super().__init__()
        self.size = size
        self.image= pygame.image.load(f'assets/{spriteName}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animation.get(spriteName)
        self.animation = False
        
    def animate(self, loop = False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if not loop :
                    self.stop_animation()
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)
        

    def start_animation(self):
        self.animation = True
    
    def stop_animation(self):
        self.animation = False
        

def load_animation_image(spriteName):
    images = []
    path = f'assets/{spriteName}/{spriteName}'
    for num in range (1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    
    return images

animation = {
    'mummy' :  load_animation_image('mummy'),
    'player' : load_animation_image('player'),
    'alien' : load_animation_image('alien'),
}