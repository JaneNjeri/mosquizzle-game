# main_menu.py

"""

This section displays a menu with options to play each game or exit.
The user's choice is then used to call the corresponding game function.
The loop continues until the user chooses to exit (option 0)

"""

# import functions from the modules
from modules.mos_control import MalariaControlGame
from modules.mos_genus_quizzle import MosGenusGuessingGame
from modules.mos_species_quizzle import MosSpeciesGuessingGame


def display_menu():
    print('Welcome to Mos_quizzle - The Game Menu!')
    print('1. Control mosquito population')
    print('2. Guess mosquito genus based on features')
    print('3. Guess mosquito species based on features')
    print('0. Exit')

def play_game1():
    print('Starting Game 1...')
    game_instance = MalariaControlGame()
    game_instance.play()

def play_game2():
    print('Starting Game 2...')
    game_instance = MosGenusGuessingGame()
    game_instance.play()

def play_game3():
    print('Starting Game 3...')
    game_instance = MosSpeciesGuessingGame()
    game_instance.play()

def main():
    print('***********************************')
    print('*           Mos_quizzle           *')
    print('***********************************')

    while True:
        display_menu()
        choice = input('Enter your choice (0-3): ')

        if choice == '1':
            play_game1()
        elif choice == '2':
            play_game2()
        elif choice == '3':
            play_game3()
        elif choice == '0':
            print('Exiting. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 0 and 3.')

if __name__ == '__main__':
    main()
