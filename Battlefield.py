from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Rexy", 250, 1000)
        self.robot = Robot("Optimus", 1000)
        self.active_weapon = Weapon("Sword", 100)
    def run_game(self):
        battlefield_one = Battlefield()
        battlefield_one.display_welcome()
        battlefield_one.battle_phase()
        battlefield_one.display_winner()

    def display_welcome(self):
         print("\nWelcome to the most epic duel of the century!\nThere will only be ONE victor, so let us begin!\n")

    def battle_phase(self):
         while self.dinosaur.dinosaur_still_alive() and self.robot.robot_still_alive():
            self.robot.robot_attack(self.dinosaur)
            print(f"{self.robot.name} attacked {self.dinosaur.name} with it's {self.active_weapon.name}, now {self.dinosaur.name} health is at {self.dinosaur.health}")

            self.dinosaur.dinosaur_attack(self.robot)
            print(f"{self.dinosaur.name} attacked {self.robot.name}, now {self.robot.name} health is at {self.robot.health}")
           
           

    def display_winner(self):
        print(f"THE FIGHT IS OVER {self.dinosaur.name} WINS!")


