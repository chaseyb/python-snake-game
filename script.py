# Python Modules 
import pygame
import sys 
import random

# defines the snake 
class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
    
    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
            
    def move(self):
        pass
    
    def reset(self):
        pass
        
    def draw(self, surface):
        pass
    
    def handle_keys(self):
        pass

# defines food the snake eats
class food(object):
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(surface):

# defines game window and controls 
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# defines the main game loop
def main ():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake ()
    food = food ()

# defines the score method 
score = 0
    while (True)
        clock.tick(10)
        #handle events
        screen.blit(surface, (0, 0))
        pygame.display.update()

main()