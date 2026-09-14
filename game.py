from goblin import Goblin


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
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
