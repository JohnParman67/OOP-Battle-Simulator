from goblin import Goblin


<<<<<<< HEAD
ARENA_NAME = "The Arena"
=======
ARENA_NAME = "Tung Tung SaGame"
>>>>>>> feature/second-goblin


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
<<<<<<< HEAD
    print("😂✌️")
    print("The gates are opening...")

    goblin = Goblin("Goblin Guy")
=======
    print("✌️ 😂")
    print("The gates are opening...")

    goblin = Goblin("GoblinDude")
    goblin2 = Goblin("GoblinGuy")
>>>>>>> feature/second-goblin

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
