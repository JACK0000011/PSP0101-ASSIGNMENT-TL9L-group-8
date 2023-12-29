import pygame
import sys
import time

#creating player sprite for game
class Player(pygame.sprite.Sprite):
    def __init__(self,pos) :
        super().__init__()
        #player size
        self.image = pygame.Surface((32,32))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        #physics of player
        self.jump_velocity = -20
        self.speed = 5
        self.gravity = 5

        #control movement using vector
        #vector2 = (x,y)two arguments
        self.direction = pygame.math.Vector2(0,0)
    #enable the player to move around
    
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        self.jump_state =False
        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump_state =True
        else:
            self.jump_state=False
            print("Jump ready")
            if not self.jump_state:
                print('jump')
            
           
    #apply a gravity to make player fall back
    def apply_grav (self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        

    def jump(self):
        self.direction.y = self.jump_velocity

      


    def update(self):
        self.get_input()

        