import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps=60

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jail break Jump")

#define game variables
main_menu = True

#setting the tile size and background image
tile_size = 50
back_img = pygame.image.load('pictures/background2.jpg')
grey_img = pygame.image.load('pictures/stone.jpg')
replay_img = pygame.image.load('pictures/replay.png')
play_img = pygame.image.load('pictures/play.png')
exit_img = pygame.image.load('pictures/exit.png')

#drawing a grid for each tile
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
          
class Button():
     def __init__(self,x,y,image):
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.x =  x
          self.rect.y = y 
          self.clicked = False
          

     def draw(self):
          action = False

          #get mouse position
          pos = pygame.mouse.get_pos()

          #check mouseover and clicked conditions
          if self.rect.collidepoint(pos):
               if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                    action = True
                    self.clicked = True

          if pygame.mouse.get_pressed()[0] == 0 :
               self.clicked = False

          #draw button
          screen.blit(self.image,self.rect)

          return action

class Player():
     def __init__(self,x,y) :
          self.reset(x,y)

     #updating the player movement
     def update (self):
          
          dx = 0
          dy = 0
          #detect if key is pressed
          key = pygame.key.get_pressed()
          #adding a condition for not double jumping
          if key[pygame.K_SPACE] and self.jumped == False and self.jump_state >=15:                
               self.velo_y = -15
               self.jump_state = 0
               self.jumped = True

          if key[pygame.K_SPACE]  == False:
               self.jump_state += 1
               self.jumped = False
          
          if key [pygame.K_a]:
               dx -=3
          if key [pygame.K_d]:
               dx += 3
          #adding gravity to player
          self.velo_y += 1
          if self.velo_y > 10:
               self.velo_y = 10
          dy += self.velo_y          

          #check for collision 
          self.in_air = True
          for tile in world.tile_list:
               #check collision in horizontal direction
               if tile[1].colliderect(self.rect.x+dx,self.rect.y, self.width,self.height):
                    dx = 0
               #check collision in vertical direction
               if tile[1].colliderect(self.rect.x,self.rect.y+dy, self.width,self.height):
                  #check if below the ground  -jumping
                    if self.velo_y < 0:
                         dy = tile[1].bottom -self.rect.top
                         self.velo_y = 0
                    #check if above the ground  -falling
                    if self.velo_y > 0:
                         dy = tile[1].top -self.rect.bottom
                         self.velo_y = 0
                         self.in_air = False

            #update player position
          self.rect.x += dx
          self.rect.y += dy 
          if self.rect.bottom >screen_height:
               self.rect.bottom = screen_height
               dy = 0  


          screen.blit(self.image,self.rect)
          pygame.draw.rect(screen,(255,255,255),self.rect,2)

     def reset(self,x,y):
          img = pygame.image.load('pictures/blue.jpg')
          self.image = pygame.transform.scale(img,(40,70))
          self.rect = self.image.get_rect()
          self.rect.x =x 
          self.rect.y =y
          self.width= self.image.get_width()
          self.height= self.image.get_height()
          self.velo_y = 0
          self.jump_state = 0
          self.jumped = False
          self.in_air = True

#create a class for game world and setting the tiles
class World():
      
      def __init__ (self,data):
            self.tile_list = []
            row_count = 0
            for row in data :
                  col_count = 0
                  for tile in row:
                        if tile == 1:
                              img = pygame.transform.scale(grey_img,(tile_size,tile_size))
                              img_rect = img.get_rect()
                              img_rect.x = col_count * tile_size
                              img_rect.y = row_count * tile_size
                              tile = (img,img_rect)
                              self.tile_list.append(tile)
                        col_count += 1
                  row_count += 1

      def draw(self):
        for tile in self.tile_list:
            screen.blit( tile[0],tile[1])
            pygame.draw.rect(screen,(255,255,255),tile[1],2)
           

world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
[1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1],
[1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]          

#instance for world and Player
player = Player(100,screen_height-130)
world=World(world_data)

#create buttons
replay_button = Button(screen_width // 2 - 50 , screen_height // 2 + 100 , replay_img)
play_button = Button(screen_width // 2 - 350 , screen_height // 2 , play_img)
exit_button = Button(screen_width // 2 + 150 , screen_height // 2 , exit_img) 

run = True
while run :
    clock.tick(fps)
    screen.blit(back_img,(0,0))
    player.update()
    draw_grid()
 
    if main_menu == True:
      if exit_button.draw():
           run = False
      if play_button.draw():
           main_menu = False
    else:
         world.draw()
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit