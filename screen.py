import pygame
import constants
from constants import GREEN, GAME_FIELD
from pygame.examples.scrap_clipboard import screen

screen= pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
def default_window():
    color=GREEN
def draw_bush():
    bush= pygame.image.load("C:\ Users\jbt\Downloads\נספחים\נספחים\ bin\grass").convert()
    from game_field import GAME_FIELD
    import random
    for i in range(20):
        random_row = random.randint(25)
        random_col= random.randint(50)
        place=(random_row,random_col)
        #צריך לתרגם את המספר רנדום מאינדקס לקואורדינטות
        screen.blits(bush,place)

# welcome_message=draw_massage


