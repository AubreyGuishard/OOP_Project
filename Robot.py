from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon

    def robot_attack(self, dinosaur):
        self.attack -= dinosaur.health

