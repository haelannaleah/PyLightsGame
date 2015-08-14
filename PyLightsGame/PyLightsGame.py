######################################################
# PyLights - a text binary puzzle game
#
# by Annaleah Ernst, Summer 2015
######################################################
from random import randrange

# map for solving puzzle in minimum number of moves
def getSolMatrix(l):
    n = len(l)
    sol = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if l[i][j]:
                for k in range(n):
                    sol[i][k] += 1
                    sol[k][j] += 1

                sol[i][j] -= 1

    sol = [[elem % 2 for elem in row] for row in sol]
    return sol

# plays the game for you based on the solution map
def autoPlay(board):
    n = len(board)
    solution = getSolMatrix(board)
    for row in board: print row
    l = board
    while sum((sum(row) for row in l)):
        for i in range(n):
            for j in range(n):
                if solution[i][j]:
                    for k in range(n):
                        board[i][k] = 1 - l[i][k]
                        board[k][j] = 1 - l[k][j]

                    print("Coordinates to flip (row, col): " + str(i + 1) + ", " + str(j + 1))
                    raw_input()
                    board[i][j] = 1 - board[i][j]
                    for row in board: print row

    print("Solution reached in " + str(sum((sum(row) for row in solution))) + " moves.")

# text based version of the lights game
# toggling an element will flip all elements in its row and column
while True:
    try:
        dimensions = eval(raw_input("Dimensions of board (even puzzles guarenteed solvable): "))
        break
    except:
        continue

board = [[randrange(0,2) for _ in range(dimensions)] for _ in range(dimensions)]

if (("n" if dimensions % 2 else raw_input("Do you want to autoplay? (y/n): ")) == "y"):
    print("Initiating autoplay. Press Enter to advance play.")
    autoPlay(board)
else:
    counter = 0
    while sum((sum(row) for row in board)):
        for row in board: print row
        while True:
            try:
                row, col = tuple(eval(raw_input("Coordinates of flippage (row,col): ")))
                break
            except:
                continue
        row -= 1
        col -= 1

        for i in range(len(board)):
            board[row][i] = 1 - board[row][i]
            board[i][col] = 1 - board[i][col]

        board[row][col] = 1 - board[row][col]
        counter += 1

    print("Congratulations! You won in " + str(counter) + " moves!")