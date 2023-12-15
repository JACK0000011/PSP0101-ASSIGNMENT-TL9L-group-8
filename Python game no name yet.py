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
from time import sleep

#initiate the pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Jump")

#directory for our game's picture
new_working_directory = "C:\pictures for multimedia assignment"
os.chdir(new_working_directory)

#image of character
original_niniimage = pygame.image.load("test.png")
image_width = 150
image_height = 200

#control scale of character
niniimage = pygame.transform.scale(original_niniimage, (image_width, image_height))
#control position of character/image
image_position = (280,250)


#loop for pygame not closing in program(important)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    screen.fill((8,131,226))

    screen.blit(niniimage, image_position)
    pygame.display.flip()
    pygame.time.delay


    pygame.quit




