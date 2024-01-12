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



import pygame
import pygame_menu
from pygame_menu import themes
from k import run_game

# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((400, 300))

# Event
update_loading = pygame.USEREVENT + 0

def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)

def progress_menu():
    mainmenu._open(progress)

def quit_game():
    exit()

# Menu initialization
mainmenu = pygame_menu.Menu('Welcome', 400, 300, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name:', default='username')
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Progress', progress_menu)
mainmenu.add.button('Quit', quit_game)

# Define 'loading' and 'progress' menus
loading = pygame_menu.Menu('Loading the Game...', 400, 300, theme=themes.THEME_ORANGE)
loading.add.progress_bar('Progress', progressbar_id='1', default=0, width=200)

progress = pygame_menu.Menu('Select a file to continue', 400, 300, theme=themes.THEME_BLUE)

# Game loop
loading_progress = 0 

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mainmenu.get_current().get_selected_widget().select()

    if mainmenu.is_enabled() and mainmenu.get_current() == loading:
        loading_progress += 1
        loading_progress = min(loading_progress, 100)  # Cap the progress at 100
        loading.get_widget('1').set_value(loading_progress)

        if loading_progress == 100:
            pygame.time.set_timer(update_loading, 0)
            mainmenu.disable()
            surface.fill((255, 255, 255))  
            run_game(surface)          
    
    mainmenu.update(events)
    mainmenu.draw(surface)
    pygame.display.update()

pygame.quit()


   