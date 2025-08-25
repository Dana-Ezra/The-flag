from math import floor
import pygame
import constants
from constants import GREEN, GAME_FIELD
import bush
from pygame.examples.scrap_clipboard import screen

SCREEN = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
def default_window(screen):
    screen.fill(GREEN)
    pygame.display.flip()
    return screen

from game_field1 import game_field
from game_field1 import create_matrix

def from_matrix_screen(screen):
    dict_x = {}
    dict_y = {}
    for x in screen:
        index_x = floor(x/10-1)
        dict_x[x]=index_x
    for y in screen:
        index_y = floor(y/10-1)
        dict_y[y]= index_y
    return dict_x,dict_y

def draw_bush():
    import random
    bush_drawing= pygame.image.load("bush.py")
    for i in range(20):
        random_row = random.randint(250)
        random_col= random.randint(500)
        place=(random_row,random_col)
        # for place[0]:

        SCREEN.blits(bush_drawing, ())
        pygame.display.update()





        #צריך לתרגם את המספר רנדום מאינדקס לקואורדינטות
        screen.blits(bush,place)

# welcome_message=draw_massagee


default_window(SCREEN)
