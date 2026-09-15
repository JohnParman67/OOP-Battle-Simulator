from dragon import Dragon
from hero import Hero
import time

ARENA_NAME = "Big Scary Battle"

def battle(hero: Hero, enemy: Dragon):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} has won the battle")
    else:
        print(f"{enemy.name} won the battle")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    time.sleep(0.1)
    file = open("asciiArt.txt")
    print(file.read())
    time.sleep(5)
    print("✌️ 😂")
    print("The gates are opening...")

    dragon = Dragon("Dragon")
    dragon2 = Dragon("Dragon2")

    print(f"{dragon.name} enters the arena with {dragon.health} health.")
    print(f"{dragon2.name} enters the arena with {dragon2.health} health.")
    placeholderName = input("Name your Hero: ")
    print(f"You're hero is {placeholderName}")
    placeholderClass = input("Name your Hero's Rank: ")
    print(f"You're hero is {placeholderName}")
    hero = Hero(placeholderName, 100, 20, placeholderClass)
    print(f"{str(hero.heroClass)} {str(hero.name)} enters")
    battle(hero, dragon)

if __name__ == "__main__":
    main()
    
