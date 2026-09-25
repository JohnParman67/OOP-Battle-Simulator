import random
from enemy import Enemy


class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=8)
        self.gold = 0

    def steal(self, hero):
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("git rekt noob")