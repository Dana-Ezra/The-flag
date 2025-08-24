from xml.etree.ElementPath import xpath_tokenizer

import pygame
import constants
from constants import GREEN, GAME_FIELD
from pygame.examples.scrap_clipboard import screen

SCREEN = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
def default_window(screen1):
    screen.fill(GREEN)
    pygame.display.flip()
    return screen1

from game_field1 import game_field
from game_field1 import create_matrix
from game_field1 import from_matrix_screen

def draw_bush():
    bush= pygame.image.load("C:\ Users\jbt\Downloads\נספחים\נספחים\ bin\grass").convert()
    import random

    for i in range(20):
        random_row = random.randint(25)
        random_col= random.randint(50)
        place=(random_row,random_col)
        for place[0]:





        #צריך לתרגם את המספר רנדום מאינדקס לקואורדינטות
        screen.blits(bush,place)

# welcome_message=draw_massagee