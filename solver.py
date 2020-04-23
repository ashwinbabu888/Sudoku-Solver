board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# solves the puzzle
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        // Munjal: One thing you can do make this faster is to keep track of
        // possible digits for each cell instead of computing everytime.
        // You can get quite fancy in how you do this:
        // 1. Simple version: keep a list of possible digits for each cell
        // 2. Keep a list of used digits per row, column and sub-grid
        // 3. Use bits to keep track of which digits are used (or unused).
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            // Munjal: Try one challenge if you are interested: do this without
            // recursion. Your core logic will be same, just needs a slighly different
            // approach.
            if solve(bo):
                return True

            bo[row][col] = 0

    return False


# checks if a number is valid in the square according to Sudoku rules
def valid(bo, num, pos):
    # checks row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # checks column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # checks individual squares
    bo_x = pos[1] // 3
    bo_y = pos[0] // 3

    for i in range(bo_y * 3, bo_y * 3 + 3):
        for x in range(bo_x * 3, bo_x * 3 + 3):
            if bo[i][x] == num and (i, x) != pos:
                return False

    return True


# creates game board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - -')

        for x in range(len(bo[0])):
            if x % 3 == 0 and x != 0:
                print(' | ', end="")

            if x == 8:
                print(bo[i][x])
            else:
                print(str(bo[i][x]) + ' ', end="")


# finds the empty spaces (returns in row by column)
def find_empty(bo):
    for i in range(len(bo)):
        for x in range(len(bo[0])):
            if bo[i][x] == 0:
                return (i, x)

    return None


solve(board)
print_board(board)
