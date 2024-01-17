class Player():
     def __init__(self,x,y) :
          self.images_right = []
          self.index = 0
          self.counter = 0
          for num in range(1, 3):
               img_right = pygame.image.load(f'pictures/walking{num}.png')
               img_right = pygame.transform.scale(img_right,(40,80))
               self.images_right.append(img_right)
          self.image = self.images_right[self.index]
          self.rect = self.image.get_rect()
          self.rect.x =x 
          self.rect.y =y
          self.width= self.image.get_width()
          self.height= self.image.get_height()
          self.velo_y = 0
          self.jump_state = 0
          self.jumped = False


     #updating the player movement
     def update(self):
          dx = 0
          dy = 0
          walk_cooldown = 5

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
               self.counter +=1
          if key [pygame.K_d]:
               dx += 3
               self.counter +=1
          if key[pygame.K_a] == False and key[pygame.K_d] == False :
               self.counter = 0
               self.index = 0
               self.image = self.images_right[self.index]



          # handle animation
          if self.counter > walk_cooldown:
               self.counter = 0
               self.index += 1
               if self.index >= len(self.images_right):
                    self.index = 0
               self.image = self.images_right[self.index]