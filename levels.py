import pygame
from tiles import Tile
from settings import tile_size
from Player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift=(0)
    
    #numerate the row and column into number to show the tile position
    def setup_level(self,layout):
        #level settings

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
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
    



    #make the world shift
    def run(self):

        #level tiles update
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        #player update
        self.player.update()
        self.player.draw(self.display_surface)
       
