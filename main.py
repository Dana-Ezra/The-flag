import pygame
import screen
from screen import default_window

open_window=True
def main():
    pygame.init()
    default_window()
    while open_window:
        arrow_direction=pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                open_window=False
            elif kk

