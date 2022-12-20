from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Sword", 100)

    def robot_attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power

    def robot_still_alive(self):
        return self.health > 0
             

