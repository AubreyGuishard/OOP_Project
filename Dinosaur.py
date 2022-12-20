class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def dinosaur_attack(self, robot):
        robot.health-= self.attack_power
        
        

    def dinosaur_still_alive(self):
        return self.health > 0