#! usr/bin/python3 -i

"""
Embark on an entertaining Mosquito Safari with this Python-based guessing game!
Your mission: identify Anopheles mosquito species by answering engaging questions
related to their distinctive characteristics.

"""

import random
import json

class AnoSpeciesGuessingGame:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config_data = json.load(file)

        self.mosquito_species = self.config_data.get('mosquito_species', [])

    def display_species_options(self):
        print('Available Anopheles mosquito species to choose from:')
        for i, species in enumerate(self.mosquito_species, 1):
            print(f"{i}. {species['name']}")

    def display_features(self, features):
        print('Features:')
        for i, feature in enumerate(features, 1):
            print(f'{i}. {feature}')

    def play(self):
        print('Welcome to the Anopheles Mosquito Species Guessing Game!')

        while True:
            self.display_species_options()
            selected_species = random.choice(self.mosquito_species)
            features_to_guess = selected_species.get('features', [])

            print('\nGuess the Anopheles mosquito species based on the following features:')
            self.display_features(features_to_guess)

            user_input = input('Enter the number corresponding to your guess: ')
            user_answer = int(user_input)

            if 1 <= user_answer <= len(self.mosquito_species):
                user_selected_species = self.mosquito_species[user_answer - 1]['name']
                if user_selected_species == selected_species['name']:
                    print("Congratulations! You've correctly identified the Anopheles mosquito species:", selected_species['name'])
                else:
                    print(f"Incorrect! The correct species is: {selected_species['name']}")
            else:
                print('Invalid input. Please enter a number corresponding to your guess.')

            retry = input('Do you want to guess again? (y/n): ').lower()
            if retry != 'y':
                print('Thanks for playing! Exiting the game.')
                break

if __name__ == '__main__':
    config_file = 'anopheles_species_config.json'
    game = AnoSpeciesGuessingGame(config_file)
    game.play()
