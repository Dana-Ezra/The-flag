from constants import GAME_FIELD
import random

def create_matrix(matrix):
    for i in range(25):
        list1 = []
        for j in range(50):
            list1.append((i,j))
        matrix.append(list1)
        list1 = []
    return matrix

create_matrix(GAME_FIELD)

from constants import SCREEN
def dict_value(matrix):
    dict1 = {}
    for i in matrix:
        for j in i :
          for x,y in SCREEN:
              dict1[(i,j)]= (x,y)
    return dict1

def flag_in_field(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if i>=20 and j>=46:
              matrix[i][j] ="Flag"
    return print(matrix)

flag_in_field(GAME_FIELD)






