import random

# Global Variables
quit = False
puzzle = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', '*']]
# We need to know the start position
# vertical_index = 3
# horizontal_index = 3


# Generates a new puzzle by shuffling the positions
def generate_puzzle(new_puzzle):
    for row in new_puzzle:
        random.shuffle(row)
    random.shuffle(new_puzzle)


# Find the starting position
def find_position(new_puzzle):
    for row in range(len(new_puzzle)):
        for col in range(len(new_puzzle[row])):
            if new_puzzle[row][col] == '*':
                return row, col


def horizontal_swap(new_index, vertical_index, horizontal_index):
    if new_index < 0 or new_index > 3:
        print('--------------')
        print('ERROR: ')
        print('Invalid move!')
        print('--------------')
        return horizontal_index
    else:
        tmp = puzzle[vertical_index][new_index]
        puzzle[vertical_index][new_index] = puzzle[vertical_index][horizontal_index]
        puzzle[vertical_index][horizontal_index] = tmp
        horizontal_index = new_index
        return horizontal_index


def vertical_swap(new_index, vertical_index, horizontal_index):
    if new_index < 0 or new_index > 3:
        print('--------------')
        print('ERROR: ')
        print('Invalid move!')
        print('--------------')
        return vertical_index
    else:
        tmp = puzzle[new_index][horizontal_index]
        puzzle[new_index][horizontal_index] = puzzle[vertical_index][horizontal_index]
        puzzle[vertical_index][horizontal_index] = tmp
        vertical_index = new_index
        return vertical_index

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
    generate_puzzle(puzzle)
    vertical_index, horizontal_index = find_position(puzzle)
    while not quit:
        print_menu()
        command = int(input("\nEnter command: "))
        if command == 1:
            new_index = horizontal_index - 1
            horizontal_index = horizontal_swap(new_index, vertical_index, horizontal_index)
        elif command == 2:
            new_index = horizontal_index + 1
            horizontal_index = horizontal_swap(new_index, vertical_index, horizontal_index)
        elif command == 3:
            new_index = vertical_index - 1
            vertical_index = vertical_swap(new_index, vertical_index, horizontal_index)
        elif command == 4:
            new_index = vertical_index + 1
            vertical_index = vertical_swap(new_index, vertical_index, horizontal_index)
        elif command == 0:
            quit = True