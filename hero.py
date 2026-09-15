import random
import time 
from dragon import Dragon

class Hero:
    #"""A playable character who battles enemies in the arena."""
    def __init__(self, heroName, heroHealth, heroPower, heroClass):
        self.name = heroName
        self.health = heroHealth
        self.attack_power = heroPower
        self.heroClass= heroClass
    
    def attack(self, dragon: Dragon):
        print(f"{self.name} attacks the Dragon")
        time.sleep(0.5)
        dragon.take_damage(random.randint(1, self.attack_power))

    def take_damage(self):
        print(f"The Dragon attacks {self.name}")
        time.sleep(0.5)
        self.health = self.health - random.randint(1, 15)
        print(f"Hero Health after attack: {str(self.health)}")
        if self.health < 1:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            print(f"Hero is alive?: {str(True)}")
    pass
