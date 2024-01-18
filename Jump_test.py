import pygame
from pygame.locals import *
from world_data_editor import *
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps=60
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jail break Jump")

#define game variables
main_menu = True
level=1
game_over = 0
tile_size = 50
max_level = 10

#setting the image
back_img = pygame.image.load('pictures/background2.jpg')
grey_img = pygame.image.load('pictures/stone.jpg')
replay_img = pygame.image.load('pictures/replay.png')
play_img = pygame.image.load('pictures/play.png')
exit_img = pygame.image.load('pictures/exit.png')
portal_img = pygame.image.load('pictures/portal.jpg')

def reset_level(level):
     player.reset(100,screen_height - 130)
     portal_group.empty()

     # if path.exists(f'level_{level}.data'):
     #      pickle_in = open (f'level_{level}.data','rb')
     #      world_data = pickle.load(pickle_in)
     # world=World(world_data)

     return world

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
     def update (self,game_over):

          dx = 0
          dy = 0
               #detect if key is pressed
          if game_over == 0:   
               key = pygame.key.get_pressed()
               #adding a condition for not double jumping
               if key[pygame.K_SPACE] and self.jumped == False and self.jump_state >=15:                
                    self.velo_y = -15
                    self.jump_state = 0
                    self.jumped = True
                    if self.sprint:
                         self.velo_y = -20
          
               if key[pygame.K_SPACE]  == False:
                    self.jump_state += 1
                    self.jumped = False
                    
               #adding a sprint status to make the player jump further
               if key[pygame.K_a] and key[pygame.K_LSHIFT]:
                    dx -=3
                    self.sprint = True
               if key[pygame.K_d] and key[pygame.K_LSHIFT]:
                    dx +=3
                    self.sprint = True
               #horizontal movement
               if key [pygame.K_a]:
                    dx -=2
                    self.sprint = False
               if key [pygame.K_d]:
                    dx += 2
                    self.sprint = False
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
                    #determine if a player is collide with portal and change his level
                    if pygame.sprite.spritecollide(self,portal_group,False):
                              game_over = 1

                    #           print('changing level')
                    
                         

               #update player position
               self.rect.x += dx
               self.rect.y += dy

               




               screen.blit(self.image,self.rect)
               pygame.draw.rect(screen,(255,255,255),self.rect,2)

               return game_over

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
                        if tile == 2:
                             portal = Portal(col_count * tile_size ,row_count * tile_size-(tile_size // 1.5))
                             portal_group.add(portal)
                        col_count += 1
                  row_count += 1
                          

      def draw(self):
        for tile in self.tile_list:
            screen.blit( tile[0],tile[1])
            pygame.draw.rect(screen,(255,255,255),tile[1],2)
#create a class for portal
class Portal(pygame.sprite.Sprite):
          def __init__(self,x,y):
               pygame.sprite.Sprite.__init__(self)
               img = pygame.image.load('pictures/portal.jpg')
               self.image = pygame.transform.scale(img,(tile_size,int(tile_size*1.5)))
               self.rect = self.image.get_rect()
               self.rect.x = x
               self.rect.y = y
               

portal_group = pygame.sprite.Group()

#instance for Player
player = Player(100,screen_height-130)

# if path.exists(f'level_{level}.data'):
#      pickle_in = open (f'level_{level}.data','rb')
#      world_data = pickle.load(pickle_in)
world=World(world_data_9)
     


#create buttons
replay_button = Button(screen_width // 2 - 50 , screen_height // 2 + 100 , replay_img)
play_button = Button(screen_width // 2 - 350 , screen_height // 2 , play_img)
exit_button = Button(screen_width // 2 + 150 , screen_height // 2 , exit_img) 

run = True
while run :
    clock.tick(fps)
    screen.blit(back_img,(0,0))
    
 
    if main_menu == True:
      if exit_button.draw():
           run = False
      if play_button.draw():
           main_menu = False
    else:
         world.draw()
         player.update(game_over)
         portal_group.draw(screen) 
              
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit