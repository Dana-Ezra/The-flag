import random
game_field = []

def create_matrix(matrix):
    for i in range(25):
        list1 = []
        for j in range(50):
            list1.append((i,j))
        matrix.append(list1)
        list1 = []
    return matrix

game_field = create_matrix(game_field)

def flag_in_field(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          if i>=20 and j>=46:
             matrix[i][j]="Flag"
    return matrix

game_field = flag_in_field(game_field)

def soldier_in_board(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i<=3 and j<=1:
              matrix[i][j]="Soldier"
    return matrix


game_field = soldier_in_board(game_field)

def mine_in_board(matrix):
 for i in range(20):
    x = random.randint(0,25)
    y = random.randint(0,50)
    if not x==0 and not y==0 and matrix[x][y]!="Flag" and matrix[x][y]!="Soldier":
      matrix[x][y]="Mine"
 return matrix

game_field = mine_in_board(game_field)


