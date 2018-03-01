# Global Variables
quit = False
puzzle = [['a', 'b', 'c', 'd'],
          ['e', 'f', 'g', 'h'],
          ['i', 'j', 'k', 'l'],
          ['m', 'n', 'o', '*']]
# We need to know the start position
horizontal_index = 3
vertical_index = 3


def print_menu():
    print('\n********* PY-PUZZLE *********\n')
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
    while not quit:
        print_menu()
        command = int(input("\nEnter command: "))
        if command == 1:
            tmp = puzzle[vertical_index][horizontal_index - 1]
            puzzle[vertical_index][horizontal_index - 1] = puzzle[vertical_index][horizontal_index]
            puzzle[vertical_index][horizontal_index] = tmp
            horizontal_index -= 1
        elif command == 2:
            tmp = puzzle[vertical_index][horizontal_index + 1]
            puzzle[vertical_index][horizontal_index + 1] = puzzle[vertical_index][horizontal_index]
            puzzle[vertical_index][horizontal_index] = tmp
            horizontal_index += 1
        elif command == 3:
            tmp = puzzle[vertical_index - 1][horizontal_index]
            puzzle[vertical_index - 1][horizontal_index] = puzzle[vertical_index][horizontal_index]
            puzzle[vertical_index][horizontal_index] = tmp
            vertical_index -= 1
        elif command == 4:
            tmp = puzzle[vertical_index + 1][horizontal_index]
            puzzle[vertical_index + 1][horizontal_index] = puzzle[vertical_index][horizontal_index]
            puzzle[vertical_index][horizontal_index] = tmp
            vertical_index += 1
        elif command == 0:
            quit = True