#! usr/bin/python3 -i

"""
Simple text-based game in Python that prompts the user with questions related to mosquito characteristics
and asks them to guess the correct mosquito genus.
The game uses a list of predefined mosquito genus for the user to guess.

"""

import random
import json

class MosGenusGuessingGame:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config_data = json.load(file)

        self.mosquito_genus = self.config_data.get('mosquito_genera', [])

    def display_genus_options(self):
        print('Available mosquito genus to choose from:')
        for i, genus in enumerate(self.mosquito_genus, 1):
            print(f"{i}. {genus['name']}")

    def display_features(self, features):
        print('Features:')
        for i, feature in enumerate(features, 1):
            print(f'{i}. {feature}')

    def play(self):
        print('Welcome to the Mosquito Genus Guessing Game!')

        while True:
            self.display_genus_options()
            selected_genus = random.choice(self.mosquito_genus)
            features_to_guess = selected_genus.get('features', [])

            print('\nGuess the mosquito genus based on the following features:')
            self.display_features(features_to_guess)

            user_input = input('Enter the number corresponding to your guess: ')
            user_answer = int(user_input)

            if 1 <= user_answer <= len(self.mosquito_genus):
                user_selected_genus = self.mosquito_genus[user_answer - 1]['name']
                if user_selected_genus == selected_genus['name']:
                    print("Congratulations! You've correctly identified the mosquito genus:", selected_genus['name'])
                else:
                    print(f"Incorrect! The correct genus is: {selected_genus['name']}")
            else:
                print('Invalid input. Please enter a number corresponding to your guess.')

            retry = input('Do you want to guess again? (y/n): ').lower()
            if retry != 'y':
                print('Thanks for playing! Exiting the game.')
                break

if __name__ == '__main__':
    config_file = 'mos_genus_quizzle_config.json'
    game = MosGenusGuessingGame(config_file)
    game.play()
