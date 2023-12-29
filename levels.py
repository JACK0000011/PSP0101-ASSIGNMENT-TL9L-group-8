import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface 
        self.setup_level(level_data)
        #default value for the world shifting
        self.world_shift=(0)
    
  #setting up level for the game
    def setup_level(self,layout):
        #level settings

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        #numerate the row and column into number to show the tile position
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                #for showing exact coordinate for the player
                print(f'{row_index},{col_index}:{col}')

                #placing tile according to maps
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':             
                    tile= Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if col == "P":              
                     player_sprite=Player((x,y),)
                     self.player.add(player_sprite)
    # def scroll_y(self):
    #     player=self.player.sprite
    #     player_y=player.rect.centery
    #     direction_y=player.direction.y
    #     if player_y <-500:
    #         self.world_shift = -8
            

    #collide with tiles horizontally and stop the player
    def horizontal_collide(self):
        player = self.player.sprite
        #player moving horizontal (from player.py )
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                #checking if collide with left
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                #checking if collide with right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.right
                    
    #collide with tiles vertivally and stop the player
    def vertical_collide (self):
        player = self.player.sprite
        #player jumping vertically
        player.apply_grav()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                #checking if collide with bottom
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    #cancel out the gravity
                    player.direction.y = 0
                #checking if collide with top
                elif player.direction.y < 0:
                    #cancel out negative y
                    player.direction.y = 0
                    player.rect.top = sprite.rect.bottom

       
    


    #make the world shift
    def run(self):

        #level tiles update
        # self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        #player update
        self.player.update()
        self.tiles.update(self.world_shift)
        self.horizontal_collide()
        self.vertical_collide()
        self.player.draw(self.display_surface)
    

