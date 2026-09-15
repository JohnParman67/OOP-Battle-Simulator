from goblin import Goblin
from hero import Hero

ARENA_NAME = "Tung Tung SaGame"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("✌️ 😂")
    print("The gates are opening...")

    goblin = Goblin("Goblin")
    goblin2 = Goblin("GoblinGuy")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    placeholderName = input("Name your Hero: ")
    print(f"You're hero is {placeholderName}")
    placeholderClass = input("Name your Hero's Rank: ")
    print(f"You're hero is {placeholderName}")
    hero = Hero(placeholderName, 100, 20, placeholderClass)
    print(f"{str(hero.heroClass)} {str(hero.name)} enters")
    herosAttack = hero.attack(goblin)
    herotake_damage = hero.take_damage()
    heroLiving = hero.is_alive()

if __name__ == "__main__":
    main()
    
