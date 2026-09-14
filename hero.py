import random
import time 
from goblin import Goblin

class Hero:
    #"""A playable character who battles enemies in the arena."""
    def __init__(self, heroName, heroHealth, heroPower, heroClass):
        self.name = heroName
        self.health = heroHealth
        self.attack_power = heroPower
        self.heroClass= heroClass
    
    def attack(self, goblin: Goblin):
        print(f"{self.name} attacks the Goblin")
        time.sleep(0.5)
        goblin.take_damage(random.randint(1, self.attack_power))

    def take_damage(self):
        print(f"The Goblin attacks {self.name}")
        time.sleep(0.5)
        self.health = self.health - random.randint(1, 15)
        print(f"Hero Health after attack: {str(self.health)}")
        if self.health < 1:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            print(f"Hero is alive?: {str(True)}")
    pass
