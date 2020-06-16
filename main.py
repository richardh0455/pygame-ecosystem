import pygame, sys
from random import randrange
# Sets size of grid
from Cell import Cell
from Fox import Fox
from TerrainType import TerrainType
from world_generation import WorldGeneration

WINDOWMULTIPLIER = 5
WINDOWSIZE = 100
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
FPS= 5
# Set up the colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)
LIGHTGRAY = (200, 200, 200)
RED = (235, 64, 52)
BASICFONTSIZE = 20

pygame.init()
BASICFONT = pygame.font.SysFont("comicsansms", BASICFONTSIZE)
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
CELLWIDTH = 5
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
WORLDSIZE = 100
def generate_game_world():
    generator = WorldGeneration()
    return generator.generate_game_world()

def get_color():
    list = TerrainType.list()
    random = randrange(5)
    return list[random]


def draw_cell (cell, x, y, animals):
    color = cell.terrainType.value
    for animal in animals:
        if animal.location == (x/CELLWIDTH,y/CELLWIDTH):
            color = animal.color
    pygame.draw.rect(DISPLAYSURF, color, [x, y, x+CELLWIDTH, y+CELLWIDTH], 0)

def main():
    cells = generate_game_world()

    fox = Fox()
    animals = [fox]
    carryOn = True
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop

        # --- Game logic should go here

        for animal in animals:
            next_move = animal.get_next_move(cells)
            animal.update_location(next_move)

        # --- Drawing code should go here
        # First, clear the screen to white.
        DISPLAYSURF.fill(WHITE)

        rowOffset = 0
        for row in cells:
            columnOffset = 0
            for cell in row:
                draw_cell(cell, columnOffset, rowOffset, animals)
                columnOffset += CELLWIDTH
            rowOffset += CELLWIDTH

        #The you can draw different shapes and lines or add text to your background stage.
        ##pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
        ##pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        ##pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    #Once we have exited the main program loop we can stop the game engine:
    pygame.quit()

main()