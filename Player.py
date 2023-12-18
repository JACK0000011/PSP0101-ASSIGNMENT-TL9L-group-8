import pygame
from pygame.sprite import Group

#creating player sprite for game
class player(pygame.sprite.Sprite):
    def __init__(self,pos) :
        super().__init__()
        #player size
        self.image = pygame.Surface((32,32))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
    #enable the player to move around
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        pass
    