# launcher.py

"""

This script launches the game and displays a menu with options to play each game or exit.
The user's choice is then used to call the corresponding game function.
The loop continues until the user chooses to exit (option 0)

"""

import os

# import functions from the modules
from modules.mos_control import MalariaControlGame
from modules.mos_genus_quizzle import MosGenusGuessingGame
from modules.anoph_species_quizzle import AnoSpeciesGuessingGame


def display_menu():
    print('\nWelcome to Mos_quizzle - The Game Menu!')
    print('1. Control mosquito population game')
    print('2. Guess mosquito genus based on features')
    print('3. Guess mosquito species based on features')
    print('0. Exit')

def play_game1():
    print('Starting Game 1...')
    game_instance = MalariaControlGame()
    game_instance.play()

# get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

def play_game2():
    print('Starting Game 2...')
    config_file = os.path.join(current_dir, 'modules', 'mos_genus_quizzle_config.json')
    game_instance = MosGenusGuessingGame(config_file)
    game_instance.play()


def play_game3():
    print('Starting Game 3...')
    config_file = os.path.join(current_dir, 'modules', 'anopheles_species_config.json')
    game_instance = AnoSpeciesGuessingGame(config_file)
    game_instance.play()


def main():
    print('***********************************')
    print('*           Mos_quizzle           *')
    print('***********************************')

    while True:
        display_menu()
        choice = input('Select your game choice (0-3): ')

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
