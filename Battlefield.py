from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Rexy", 250, 1000)
        self.robot = Robot("Optimus", 1000, Weapon)

    def run_game(self):
        pass

    def display_welcome(self):
        print("\nWelcome to the most epic duel of the century!\nThere will only be ONE victor, so let us begin!\n")

     def battle_phase(self):
        pass

     def display_winner(self):
        pass

