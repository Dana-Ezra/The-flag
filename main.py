import pygame
import screen
from screen import SCREEN
from screen import default_window
from game_field1 import create_matrix, flag_in_field
import game_field1

open_window=True
def main():
    pygame.init()
    default_window(SCREEN)
    open_window=True
    while open_window:
        # arrow_direction=pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                open_window=False
            # elif kk
    matrix=[]
    create_matrix(matrix)
    flag_in_field(matrix)

main()