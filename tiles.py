import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size) :
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    #updating the screen tiles and maps
    def update(self,y_shift):
        self.rect.y += y_shift