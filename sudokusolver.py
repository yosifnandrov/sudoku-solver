board = [
    [4,1,0,0,7,0,0,0,5],
    [0,8,0,0,0,6,0,9,0],
    [0,0,0,5,0,0,0,0,0],
    [0,0,7,4,0,1,3,0,0],
    [5,3,0,0,0,0,0,1,2],
    [0,0,4,3,0,8,7,0,0],
    [0,0,0,0,0,4,0,0,0],
    [0,9,0,8,0,0,0,7,0],
    [7,0,0,0,6,0,0,2,8]
]


def sudoku(matrix):
    found = find_empty(matrix)
    if not found:
        return True
    row, col = found
    for i in range(1,10):
        if valid(matrix,i,(row,col)):
            matrix[row][col] = i
            if sudoku(matrix):
                return True

            matrix[row][col] = 0

    return False



def valid(matrix,num,position):
    for i in range(len(matrix[position[1]])):
        if matrix[position[0]][i] == num and not position[1] == i:
            return False

    for i in range(len(matrix)):
        if matrix[i][position[1]] == num and not position[0] == i:
            return False

    box_i = position[1] // 3
    box_j = position[0] // 3

    for i in range(box_j * 3 , box_j * 3 + 3):
        for j in range(box_i*3, box_i*3 + 3):
            if matrix[i][j] == num and not (i,j) == position:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and not i == 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[i])):
            if j % 3 == 0 and not j == 0:
                print(" | ", end='')
            if j == len(bo[i])-1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)
    return None


print_board(board)
print("_____________________________")
sudoku(board)
print_board(board)