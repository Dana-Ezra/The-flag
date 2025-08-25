from math import floor
import pygame
import constants
from constants import GREEN, GAME_FIELD
# import bush
from pygame.examples.scrap_clipboard import screen

SCREEN = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
def default_window(screen1):
    screen1.fill(GREEN)
    pygame.display.flip()
    return screen1

SCREEN = default_window(SCREEN)
from game_field1 import game_field
from game_field1 import create_matrix
from constants import WINDOW_WIDTH
from constants import WINDOW_HEIGHT
def from_matrix_screen(screen1):
    dict1={}
    for x in range(WINDOW_WIDTH):
       for y in range(WINDOW_HEIGHT):
        x_in_matrix = floor(x/10-1)
        y_in_matrix = floor(y/10-1)
        dict1[(x,y)] = (x_in_matrix,y_in_matrix)
    return dict1

dict_location =from_matrix_screen(SCREEN)

# def draw_bush():
#     import random
#     bush_drawing= pygame.image.load("bush.py")
#     for i in range(20):
#         random_row = random.randint(250)
#         random_col= random.randint(500)
#         place=(random_row,random_col)
#         # for place[0]:
#
#         SCREEN.blits(bush_drawing, ())
#         pygame.display.update()



from_matrix_screen(SCREEN)

        #צריך לתרגם את המספר רנדום מאינדקס לקואורדינטות
        # screen.blits(bush,place)

# welcome_message=draw_massageew


default_window(SCREEN)
