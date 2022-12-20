from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Rexy", 250, 1000)
        self.robot = Robot("Optimus", 1000)
        self.weapon = Weapon("Sword", 100)
    def run_game(self):
        pass

    def display_welcome(self):
         print("\nWelcome to the most epic duel of the century!\nThere will only be ONE victor, so let us begin!\n")

    def battle_phase(self):
         while self.dinosaur.dinosaur_still_alive() and self.robot.robot_still_alive():
            self.dinosaur.dinosaur_attack(self.robot)
            self.robot.robot_attack(self.dinosaur)
           

    def display_winner(self):
        pass


