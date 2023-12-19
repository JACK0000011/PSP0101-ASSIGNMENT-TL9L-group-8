import pygame
from pygame.sprite import Group

#pyhsics of the player



#creating player sprite for game
class Player(pygame.sprite.Sprite):
    def __init__(self,pos) :
        super().__init__()
        #player size
        self.image = pygame.Surface((32,32))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = int(2)

        #control movement using vector
        #vector2 = (x,y)two arguments
        self.direction = pygame.math.Vector2(0,0)
    #enable the player to move around
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1
        
        

        else:
            self.direction.x = 0
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        
        
    