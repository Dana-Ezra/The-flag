import pygame
import screen
from screen import default_window,SCREEN,draw_bush
from game_field1 import create_matrix, flag_in_field
import game_field1

open_window=True
def main():
    pygame.init()
    default_window()
    open_window=True
    while open_window:
        # arrow_direction=pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                open_window=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN :
                    screen.second_screen()

            # elif kk
        # matrix=[]
        # create_matrix(matrix)
        # flag_in_field(matrix)
        # bush=pygame.rect(100,150,  bush_drawing= pygame.image.load("C:\ Users\jbt\Downloads\נספחים\נספחים\ bin\grass.png"))
        # draw_bush()

main()