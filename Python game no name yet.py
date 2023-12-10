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
running=True
while running :
    for event in pygame.event():
        if event.type == pygame.quit():
            running = False

#Description of the game
os.system('cls')
time.sleep(2)
print("**********************")
print("welcome to --- this a small game created by university students")
time.sleep(3)
print("It's a word based adventure game")
time.sleep(3)
print("Player need to type on their keyboard to play this game")
time.sleep(3)
print("Hope you enjoy it!")
time.sleep(3)
print("**********************")
input("Press enter to continue")
time.sleep(1)
os.system('cls')

#Typing effect for the intro text
Start=": How you feel... \n"

for char in Start:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()

S1=": You have been asleep for quite some time...\n"

for char in S1:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

time.sleep(3)

S2="You open your eyes and saw an oldman is looking at you\n"
for char in S2:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

time.sleep(3)

S3="You:  Where... Where am I..."
for char in S3:
    sleep(0.15)
    sys.stdout.write(char)
    sys.stdout.flush()

S4="Mystery old man: You are encage in this dungeon..."
for char in S3:
    sleep(0.15)
    sys.stdout.write(char)
    sys.stdout.flush()






