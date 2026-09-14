from goblin import Goblin
from hero import Hero

ARENA_NAME = "Tung Tung SaGame"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("✌️ 😂")
    print("The gates are opening...")

    goblin = Goblin("GoblinDude")
    goblin2 = Goblin("GoblinGuy")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    hero = Hero("Tung Tung Sahur", 100, 20, "King")
    print(f"Sir {str(hero.name)}, the {str(hero.heroClass)} enters")
    herosAttack = hero.attack(goblin)
    herotake_damage = hero.take_damage()
    heroLiving = hero.is_alive()

if __name__ == "__main__":
    main()
    
