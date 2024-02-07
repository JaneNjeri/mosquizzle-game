#! usr/bin/python3 -i   # -i is for 'interactive' mode

"""
File: main.py
Simple text-based game in Python game that combines elements of strategy and decision-making related to controlling malaria transmission.
This game allows the player to make decisions such as attacking mosquitoes, using bed nets, 
and using insecticide to control the mosquito population and maintain their health. 
The player wins if they control the mosquito population and survive, and they lose if their health reaches zero.

"""

import random

class MalariaControlGame:
    def __init__(self):
        self.player_health = 100
        self.mosquito_population = 10
        self.bed_net_available = True
        self.insecticide_available = True
        self.days_survived = 0

    def display_stats(self):
        print(f"\nDay {self.days_survived} - Player Health: {self.player_health} | Mosquito Population: {self.mosquito_population}")
        print(f"Bed Net Available: {'Yes' if self.bed_net_available else 'No'} | Insecticide Available: {'Yes' if self.insecticide_available else 'No'}")

    def attack_mosquito(self):
        damage = random.randint(10, 20)
        self.mosquito_population -= 1
        self.player_health -= damage
        print(f"You successfully killed a mosquito! It dealt {damage} damage to you.")

    def use_bed_net(self):
        self.bed_net_available = False
        self.player_health += random.randint(5, 15)
        print("You used a bed net and gained some health.")

    def use_insecticide(self):
        self.insecticide_available = False
        self.mosquito_population -= random.randint(2, 5)
        print("You used insecticide to reduce the mosquito population.")

    def explore(self):
        self.days_survived += 1
        self.mosquito_population += random.randint(1, 3)
        self.player_health -= random.randint(5, 15)
        print("You explored the area. Mosquitoes are breeding, and your health decreased.")

    def rest(self):
        self.days_survived += 1
        self.player_health += random.randint(10, 20)
        print("You rested and regained some health.")

    def play(self):
        print("Welcome to the Malaria Control Game!")
        print("Customize your game by adjusting starting parameters.")
        self.player_health = int(input("Enter starting player health (default is 100): ") or 100)
        self.mosquito_population = int(input("Enter starting mosquito population (default is 10): ") or 10)

        while self.player_health > 0 and self.mosquito_population > 0:
            self.display_stats()
            print("\nChoose your action:")
            print("1. Attack mosquitoes")
            print("2. Use bed net")
            print("3. Use insecticide")
            print("4. Explore")
            print("5. Rest")
            print("6. Quit")

            choice = input("Enter the number corresponding to your action: ")

            if choice == '1':
                self.attack_mosquito()
            elif choice == '2':
                if self.bed_net_available:
                    self.use_bed_net()
                else:
                    print("You've already used the bed net.")
            elif choice == '3':
                if self.insecticide_available:
                    self.use_insecticide()
                else:
                    print("You've already used the insecticide.")
            elif choice == '4':
                self.explore()
            elif choice == '5':
                self.rest()
            elif choice == '6':
                print("Thanks for playing! Exiting the game.")
                break
            else:
                print("Invalid choice. Please choose again.")

        if self.player_health <= 0:
            print(f"\nGame over! You succumbed to malaria after surviving {self.days_survived} days.")
        elif self.mosquito_population <= 0:
            print(f"\nCongratulations! You successfully controlled the mosquito population and survived for {self.days_survived} days.")

if __name__ == "__main__":
    game = MalariaControlGame()
    game.play()
