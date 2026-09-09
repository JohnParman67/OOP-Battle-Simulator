from goblin import Goblin


ARENA_NAME = "The Arena"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("😂✌️")
    print("The gates are opening...")

    goblin = Goblin("Goblin Guy")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
