# import actors

import time
import random
from actors import Wizard, Creature,SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print("---------------------------------------------------")
    print("               WIZARD BATTLE APP")
    print("---------------------------------------------------")
    print()

def game_loop():
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 80, True),
        Wizard("Evil Wizard", 1000)
    ]

    hero = Wizard("Gandalf", 100)

    while True:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest.")
        print()


        cmd = input(" Do you want to [a]ttack, [r]unaway, or [l]ookaround? ")
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and takes time to recover.")
                time.sleep(5)
                print("The wizard returns revitalised.")
        elif cmd == "r":
            print("The wizard is unsure of his powers and flees!")
        elif cmd == "l":
            print(f"The wizard {hero.name} hides in the surroundings and sees.")
            for c in creatures:
                print(f" * A {c.name} of level of {c.level}")
        else:
            print("Exiting the game..bye")
            break

        if not creatures:
            print("You defeated all the creatures. Good job!")
            break


if __name__ == "__main__":
    main()


