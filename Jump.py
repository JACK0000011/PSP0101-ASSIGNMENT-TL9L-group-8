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
level = Level(level_map1,screen)



#directory for our game's picture
new_working_directory = "C:\pictures for psp0101 assignment"
os.chdir(new_working_directory)

#image of characterdd adad
    
#loop for pygame not closing in program(important)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
         
       


    screen.fill('Black')
    level.run()
    

    
    #updating the pygame display 
    pygame.display.update()
    CLOCK.tick(60)

    
    pygame.quit




