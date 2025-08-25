import pygame.image
from game_field1 import game_field
# soldier=pygame.image.load()
import os
solder_drawing=pygame.image.load(os.path.join("bin","soldier.png"))

def soldier_location(matrix):
    list_of_soldier_index = []
    for i in matrix:
        for j in i:
         if j=="Soldier":
                list_of_soldier_index.append(matrix.index("Soldier"))
         else:
             continue

    return list_of_soldier_index

list_soldier_loc = soldier_location(game_field)

def soldier_legs(index_soldier):
    list1= []
    for i in index_soldier:
      if i[0] == index_soldier(max(i[0])):
         list1.append(i)
    return print(list1)

soldier_legs(list_soldier_loc)







