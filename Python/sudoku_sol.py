board = [
    [5,0,9,0,0,0,4,0,0],
    [7,0,8,3,0,4,9,0,0],
    [6,0,1,0,0,0,7,3,0],
    [4,6,2,5,0,0,0,0,0],
    [3,8,5,7,2,0,6,4,9],
    [1,0,7,4,0,8,2,0,0],
    [2,0,0,1,0,0,0,0,4],
    [0,0,3,0,4,0,0,8,7],
    [0,7,0,0,5,3,0,0,6]
]

def solve(b):
    find = find_empty_square(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid_pos(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0
    return False

def valid_pos(b, num, pos):
    # Check row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

def find_empty_square(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)                 # row, col
    return None

print_board(board)
solve(board)
print("\nSolution:\n")
print_board(board)