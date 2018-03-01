import random

# Global Variables
quit = False
puzzle = [['a', 'b', 'c', 'd'],
          ['e', 'f', 'g', 'h'],
          ['i', 'j', 'k', 'l'],
          ['m', 'n', 'o', '*']]
# We need to know the start position
vertical_index = 3
horizontal_index = 3


# Generates a new puzzle by shuffling the positions
def new_puzzle(puzzle):
    for row in puzzle:
        random.shuffle(row)
    random.shuffle(new_puzzle)


# Find the starting position
def find_position(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == '*':
                return row, col


def print_menu():
    print('\n----------- pyPuzzle! -----------\n')
    print(puzzle[0])
    print(puzzle[1])
    print(puzzle[2])
    print(puzzle[3])
    print('\nMenu: ')
    print('0. quit')
    print('1. left')
    print('2. right')
    print('3. up')
    print('4. down')


if __name__ == '__main__':
    new_puzzle(puzzle)
    vertical_index, horizontal_index = find_position(puzzle)
    while not quit:
        print_menu()
        command = int(input("\nEnter command: "))
        if command == 1:
            new_index = horizontal_index - 1
            if new_index < 0:
                print('--------------')
                print('ERROR: ')
                print('Invalid move!')
                print('--------------')
            else:
                tmp = puzzle[vertical_index][new_index]
                puzzle[vertical_index][new_index] = puzzle[vertical_index][horizontal_index]
                puzzle[vertical_index][horizontal_index] = tmp
                horizontal_index = new_index
        elif command == 2:
            new_index = horizontal_index + 1
            if new_index > 3:
                print('--------------')
                print('ERROR: ')
                print('Invalid move!')
                print('--------------')
            else:
                tmp = puzzle[vertical_index][new_index]
                puzzle[vertical_index][new_index] = puzzle[vertical_index][horizontal_index]
                puzzle[vertical_index][horizontal_index] = tmp
                horizontal_index = new_index
        elif command == 3:
            new_index = vertical_index - 1
            if new_index < 0:
                print('--------------')
                print('ERROR: ')
                print('Invalid move!')
                print('--------------')
            else:
                tmp = puzzle[new_index][horizontal_index]
                puzzle[new_index][horizontal_index] = puzzle[vertical_index][horizontal_index]
                puzzle[vertical_index][horizontal_index] = tmp
                vertical_index = new_index
        elif command == 4:
            new_index = vertical_index + 1
            if new_index > 3:
                print('--------------')
                print('ERROR: ')
                print('Invalid move!')
                print('--------------')
            else:
                tmp = puzzle[new_index][horizontal_index]
                puzzle[new_index][horizontal_index] = puzzle[vertical_index][horizontal_index]
                puzzle[vertical_index][horizontal_index] = tmp
                vertical_index = new_index
        elif command == 0:
            quit = True