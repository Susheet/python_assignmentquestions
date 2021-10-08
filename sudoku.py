def isinRange(board):

  N = 9
  for i in range(0, N):
    for j in range(0, N):
      if ((board[i][j] <= 0) or
          (board[i][j] > 9)):
        return False 
  return True

def isValidSudoku(board):

  N = 9
  if (isinRange(board) == False):
    return False
  unique = [False] * (N + 1)
  for i in range(0, N):
      for m in range(0, N + 1):
          unique[m] = False
      for j in range(0, N):
          Z = board[i][j]
          if (unique[Z] == True):
              return False
      unique[Z] = True
  for i in range(0, N):
      for m in range(0, N + 1):
          unique[m] = False
      for j in range(0, N):
          Z = board[j][i]
          if (unique[Z] == True):
              return False 
          unique[Z] = True
  for i in range(0, N - 2, 3):
      for j in range(0, N - 2, 3):
          for m in range(0, N + 1):
              unique[m] = False
  for k in range(0, 3):
      for l in range(0, 3):
          X = i + k
          Y = j + l
          Z = board[X][Y]
          if (unique[Z] == True):
            return False
          unique[Z] = True
  return True

if __name__ == '__main__':

  board = [ [ 7, 9, 2, 1, 5, 4, 3, 8, 6 ],
            [ 6, 4, 3, 8, 2, 7, 1, 5, 9 ],
            [ 8, 5, 1, 3, 9, 6, 7, 2, 4 ],
            [ 2, 6, 5, 9, 7, 3, 8, 4, 1 ],
            [ 4, 8, 9, 5, 6, 1, 2, 7, 3 ],
            [ 3, 1, 7, 4, 8, 2, 9, 6, 5 ],
            [ 1, 3, 6, 7, 4, 8, 5, 9, 2 ],
            [ 9, 7, 4, 2, 1, 5, 6, 3, 8 ],
            [ 5, 2, 8, 6, 3, 9, 4, 1, 7 ] ]

  if (isValidSudoku(board)):
    print("Valid")
  else:
      print("Not Valid")


