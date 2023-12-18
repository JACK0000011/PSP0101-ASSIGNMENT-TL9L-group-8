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
from time import sleep
from pygame.locals import*
from levels import Level
from settings import level_map

#initiate the pygame
pygame.init()


#fps setting and main display
CLOCK = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100,100),200))
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("Jump")


#directory for our game's picture
new_working_directory = "C:\pictures for psp0101 assignment"
os.chdir(new_working_directory)

#image of character
original_niniimage = pygame.image.load("test.png")
ninijumping = pygame.image.load("test2.png")
X_pos,Y_pos =(500,600)

#physics of the game
Jumping  = False
Y_gravity = 1
Jump_height = 10
Y_velocity = Jump_height
Walking = False
Walkvelo = 1


#image of background
background1=pygame.image.load('background1.jpg')

#control scale of character
image_width = 80
image_height = 100
ninistand = pygame.transform.scale(original_niniimage, (image_width, image_height))
ninijumping = pygame.transform.scale(original_niniimage, (image_width, image_height))
nini_rect = ninistand.get_rect(center=(X_pos, Y_pos))

#control position of character/image

characterpos = X_pos,Y_pos
#function for the character

        
#loop for pygame not closing in program(important)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_SPACE]:
        Jumping=True

    # Update the display
    screen.blit(background1,(0,200))
    
    #subtracting Y pos make character move up
    if Jumping:
        Y_pos -= Y_velocity
        Y_velocity -= Y_gravity
        #make sure the character come down to ground
        if Y_velocity <- Jump_height:
            Jumping=False
            Y_velocity = Jump_height
        nini_rect=ninijumping.get_rect(center=(X_pos, Y_pos))
        screen.blit(ninijumping,nini_rect)
    else:
        nini_rect = ninistand.get_rect(center=(X_pos, Y_pos))
        screen.blit(ninistand,nini_rect)


   
            

    pygame.display.update()
    CLOCK.tick(60)

    
    pygame.quit




