# Global Variables
quit = False


def print_menu():
    print('/nMenu: ')
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
            print('You have chosen to go: left')
        elif command == 2:
            print('You have chosen to go: right')
        elif command == 3:
            print('You have chosen to go: up')
        elif command == 4:
            print('You have chosen to go: down')
        elif command == 0:
            quit = True