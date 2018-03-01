import random

# Global Variables
quit = False
# 3x3 puzzle
easy_puzzle = [['a', 'b', 'c'],
               ['d', 'e', 'f'],
               ['g', 'h', '*']]
# 4x4 puzzle
hard_puzzle = [['a', 'b', 'c', 'd'],
               ['e', 'f', 'g', 'h'],
               ['i', 'j', 'k', 'l'],
               ['m', 'n', 'o', '*']]


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


def horizontal_swap(new_index, vertical_index, horizontal_index, new_puzzle):
    if new_index < 0 or new_index > 3:
        print('--------------')
        print('ERROR: ')
        print('Invalid move!')
        print('--------------')
        return vertical_index, horizontal_index
    else:
        tmp = new_puzzle[vertical_index][new_index]
        new_puzzle[vertical_index][new_index] = new_puzzle[vertical_index][horizontal_index]
        new_puzzle[vertical_index][horizontal_index] = tmp
        horizontal_index = new_index
        return vertical_index, horizontal_index


def vertical_swap(new_index, vertical_index, horizontal_index, new_puzzle):
    if new_index < 0 or new_index > 3:
        print('--------------')
        print('ERROR: ')
        print('Invalid move!')
        print('--------------')
        return vertical_index, horizontal_index
    else:
        tmp = new_puzzle[new_index][horizontal_index]
        new_puzzle[new_index][horizontal_index] = new_puzzle[vertical_index][horizontal_index]
        new_puzzle[vertical_index][horizontal_index] = tmp
        vertical_index = new_index
        return vertical_index, horizontal_index


def print_menu(new_puzzle):
    print('\n----------- pyPuzzle! -----------\n')
    print(new_puzzle[0])
    print(new_puzzle[1])
    print(new_puzzle[2])
    # print(new_puzzle[3])
    print('\nMenu: ')
    print('0. quit')
    print('1. left')
    print('2. right')
    print('3. up')
    print('4. down')


if __name__ == '__main__':
    generate_puzzle(easy_puzzle)
    vertical_index, horizontal_index = find_position(easy_puzzle)
    while not quit:
        print_menu(easy_puzzle)
        command = int(input("\nEnter command: "))
        if command == 1:
            new_index = horizontal_index - 1
            vertical_index, horizontal_index = horizontal_swap(new_index, vertical_index, horizontal_index, easy_puzzle)
        elif command == 2:
            new_index = horizontal_index + 1
            vertical_index, horizontal_index = horizontal_swap(new_index, vertical_index, horizontal_index, easy_puzzle)
        elif command == 3:
            new_index = vertical_index - 1
            vertical_index, horizontal_index = vertical_swap(new_index, vertical_index, horizontal_index, easy_puzzle)
        elif command == 4:
            new_index = vertical_index + 1
            vertical_index, horizontal_index = vertical_swap(new_index, vertical_index, horizontal_index, easy_puzzle)
        elif command == 0:
            quit = True