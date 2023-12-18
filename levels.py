import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface 
        self.setup_level(level_data)
    
    #numerate the row and column into number to show the tile position
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                print(f'{row_index},{col_index}:{col}')

                #placing tile according to maps
                if col == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                
                    tile= Tile((x,y),tile_size)
                    self.tiles.add(tile)


    def run(self):
        self.tiles.draw(self.display_surface)