# *********************************************************
# Program: YOUR_FILENAME.py
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

#init the pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("No name game")


new_working_directory = "C:/Users/USER.MSI/Documents/GitHub/PSP0101-ASSIGNMENT-/picture"
os.chdir(new_working_directory)
original_niniimage = pygame.image.load("test.png")
image_width = 100
image_height = 75
niniimage = pygame.transform.scale(original_niniimage, (image_width, image_height))
image_position = (100,400)
walk_speed = 5

#loop for pygame not closing in program
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        image_position[0] -= walk_speed
    if keys[pygame.K_a]:
        image_position[0] += walk_speed

    # Update the display
    screen.fill((8,131,226))
    clock.tick(30)
    screen.blit(niniimage, image_position)
    pygame.display.flip()
    pygame.time.delay


    pygame.quit




