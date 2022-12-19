class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def dinosaur_attack(self, robot):
        self.attack -= robot.health
        

    def dinosaur_health(self, health):
        self.health = health