import numpy as np

# other boards:
# 

# 0 0 0 7 0 0 0 0 1 0 0 0 0 4 0 0 0 0 2 7 0 0 1 5 0 0 6 1 6 0 0 2 0 0 4 5 0 2 0 0 0 0 0 8 0 4 9 0 0 0 0 0 2 3 8 0 0 5 7 0 0 6 4 0 0 0 0 6 0 0 0 0 3 0 0 0 0 2 0 0 0

#5 1 7 6 0 0 0 3 4 2 8 9 0 0 4 0 0 0 3 4 6 2 0 5 0 9 0 6 0 2 0 0 0 0 1 0 0 3 8 0 0 6 0 4 7 0 0 0 0 0 0 0 0 0 0 9 0 0 0 0 0 7 8 7 0 3 4 0 0 5 6 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0 0 0 7 9 0 5 0 1 8 0 8 0 0 0 0 0 0 0 7 0 0 7 3 0 6 8 0 0 4 5 0 7 0 8 0 9 6 0 0 3 5 0 2 7 0 0 7 0 0 0 0 0 0 0 5 0 1 6 0 3 0 4 2 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 






def parseArray(sudoku):
  puzzle = np.array(np.split(np.array(sudoku),9))
  return puzzle

inputPuz = input("Enter a sudoku puzzle with 0s in place of blank spaces:")
print()

sudoku = inputPuz.split()
sudoku = [int(x) for x in sudoku]


puzzle = parseArray(sudoku)

# puzzle = np.array(
#          [[5,1,7,6,0,0,0,3,4],
#           [2,8,9,0,0,4,0,0,0],
#           [3,4,6,2,0,5,0,9,0],  
#           [6,0,2,0,0,0,0,1,0],
#           [0,3,8,0,0,6,0,4,7],
#           [0,0,0,0,0,0,0,0,0],
#           [0,9,0,0,0,0,0,7,8],
#           [7,0,3,4,0,0,5,6,0],
#           [0,0,0,0,0,0,0,0,0]])

clean = []
def cleaner(puzzle):#formats puzzle

    top = (puzzle[0:3])#first row
    middle = (puzzle[3:6])#second row
    bottom = (puzzle[6:10])
    spacer = np.array([["-","-","-","-","-","-","-","-","-"]])
    spacer2 = np.array([['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'], ['|']])
    middle = (np.append(middle, spacer, axis=0))#add spacer

    clean = np.append(top, spacer, axis=0)
    clean = np.append(clean, middle, axis=0)
    clean = np.append(clean, bottom, axis=0)

    left = clean[:,:3]
    middle2 = clean[:,3:6]
    end = clean[:,6:10]

    cleaner = np.append(left, spacer2, axis=1)
    middle2 = np.append(middle2, spacer2, axis=1)
    cleaner = np.append(cleaner, middle2, axis=1)
    cleaner = np.append(cleaner, end, axis=1)

    translate = {39:None}
    cleaner = str(cleaner).translate(translate)

    return cleaner

def findGrid(row, col):
  grid = []
  r = (row//3)*3
  c = (col//3)*3
  for i in range(r, r + 3):
    for n in range(c, c + 3):
      grid.append(puzzle[i][n])
      
  return grid




def getMissing(puzzle):
  for i in range(0,9):
    for j in range(0,9):
      if puzzle[i][j] == 0:
        return i, j
  return None
        
    


def isValid(row, col, num):
    
  for i in range(0,9):
      place = puzzle[row][i]
      if place == num:
        return False

  for i in range(0,9):
        place = puzzle[i,col]
        if place == num:
          return False

  grid = findGrid(row,col)
      
  for i in range(0,9):
        if(grid[i] == num):
          return False

      

      
  return True





rec = 0
def solve(puzzle):
  global rec
  missing = getMissing(puzzle)
  if not missing:
    return True
  else:
    rec+=1
    x, y = missing
    for i in range(1,10):
      if isValid(x,y,i):
        puzzle[x][y] = i

        if solve(puzzle):
          return True , rec
          
      
        puzzle[x][y] = 0

    return False

print("Your Puzzle:")
print(puzzle)
print()
print("solving...")
result, recursions = solve(puzzle)

print(cleaner(puzzle))
print()
print("There were " +str(recursions)+ " recursions" )    

