# *********************************************************
# Program: Jump.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL9L
# Year: 2023/24 Trimester 1
# Names: Tiew Fu Siang | Low Zheng Hao | Nicholas Beh Zi Yang
# IDs: 1221107343 | 1221109384 | 1221106297
# Emails: 1221107343@student.mmu.edu.my | MEMBER_EMAIL_2 | MEMBER_EMAIL_3
# Phones: 010-3706933| MEMBER_PHONE_2 | MEMBER_PHONE_3
# *********************************************************

import time
import sys
import os
import pygame
from tiles import Tile
from pygame.locals import*
from settings import *
from levels import Level

#initiate the pygame
pygame.init()


#fps setting and main display
CLOCK = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100,100),250))
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jump")

#creating the map
level = Level(level_map,screen)



#directory for our game's picture
new_working_directory = "C:\pictures for psp0101 assignment"
os.chdir(new_working_directory)

#image of character
original_niniimage = pygame.image.load("test.png")
ninijumping = pygame.image.load("test2.png")
X_pos,Y_pos =(500,600)



#image of background
# background1=pygame.image.load('background1.jpg')



#function for the character

        
#loop for pygame not closing in program(important)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    # Update the display
    # screen.blit(background1,(0,200))
    
    #subtracting Y pos make character move up (Jumping)
    # if Jumping:
    #     Y_pos -= Y_velocity
    #     Y_velocity -= Y_gravity
    #     #make sure the character come down to ground
    #     if Y_velocity <- Jump_height:
    #         Jumping=False
    #         Y_velocity = Jump_height
    #     nini_rect=ninijumping.get_rect(center=(X_pos, Y_pos))
    #     screen.blit(ninijumping,nini_rect)
    # else:
    #     nini_rect = ninistand.get_rect(center=(X_pos, Y_pos))
    #     screen.blit(ninistand,nini_rect)
    
    #making the character moving horizontally
    
    
            


    screen.fill('Black')
    level.run()
    
    

    pygame.display.update()
    CLOCK.tick(60)

    
    pygame.quit




