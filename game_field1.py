import random
from glob import translate
from math import floor
from xml.sax.handler import property_xml_string

from pygame.examples.scrap_clipboard import screen
game_field = []

def create_matrix(matrix):
    for i in range(25):
        list1 = []
        for j in range(50):
            list1.append((i,j))
        matrix.append(list1)
        list1 = []
    return matrix


def from_matrix_screen(matrix):
    dict_x = {}
    dict_y = {}
    from screen import SCREEN
    for x in SCREEN:
        index_x = floor(x/10-1)
        dict_x[x]=index_x
    for y in screen:
        index_y = floor(y/10-1)
        dict_y[y]= index_y
    return dict_x,dict_y


def dict_value(matrix1):
    dict1 = {}
    matrix = create_matrix(game_field)
    x = from_matrix_screen(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if  i in x[0].values():
                if j in x[1].values():
                    dict1[(i,j)] = (x[1].keys(x[1]))


def flag_in_field(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if i>=20:
              if j>=46:
                  matrix[i][j]="Flag"

flag_in_field(game_field)

