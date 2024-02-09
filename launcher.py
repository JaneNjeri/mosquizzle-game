# launcher.py

"""
This script serves as a launcher for the main_menu.py file, which contains
three simple text-based games.

"""

from subprocess import run

def main():
    print('Initializing the program and calling the main menu...')

    # use the subprocess module to call the main_menu.py file
    run(['python', 'main_menu.py'])

if __name__ == '__main__':
    main()
