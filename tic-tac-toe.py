
# Global Variables
quit = False
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

def print_grid(some_grid):
    print('\n------- Tic Tac Toe -------')
    print('\n  col:   1    2    3')
    for row in range(len(some_grid)):
        print('row ' + str(row + 1) + ': ' + str(some_grid[row]) + '\n')

if __name__ == '__main__':
    while not quit:
        print_grid(grid)
        print('You are "X". Please enter row and column number when prompt!')
        row = int(input('Please enter a row number: '))
        col = int(input('Please enter a column number: '))
        grid[row-1][col-1] = 'X'