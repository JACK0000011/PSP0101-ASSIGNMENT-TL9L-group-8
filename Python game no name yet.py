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
#loop for pygame not closing in program
running=True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#colour rgb
green=(68,255,0)
blue=(8,131,226)

screen.fill (green)
pygame.display.update()

X=500
Y=500

font1 = pygame.font.Font('Arial.ttf', 32)
text= font1.render('Test',True, green, blue)
textRect=text.get_rect()
textRect.center=(X//2,Y//2)






