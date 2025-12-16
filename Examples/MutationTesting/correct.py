import sys

if __name__ == "__main__":
    # check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python correct.py <water>")
        sys.exit(1)

    W = int(sys.argv[1])  # amount of water

    print("MODULE main")

    print("VAR")
    print("    action: 0..2;") # 0: nop, 1: beverage, 2: fill
    print("    beverage: 0..2;") # 0: none, 1: coffee, 2: tea
    print(f"    water: 0..{W};") # amount of water

    print("INIT")
    print(f"    beverage = 0 & water = {W}")

    print("TRANS")
    actions = []
    actions.append(f"action = 0 & next(beverage) = beverage & next(water) = water") # nop
    actions.append(f"action = 1 & water > 0 & next(beverage) > 0 & next(water) = water - 1") # beverage
    actions.append(f"action = 1 & water = 0 & next(beverage) = 0 & next(water) = water") # beverage no water
    actions.append(f"action = 2 & water = 0 & next(beverage) = 0 & next(water) = {W}") # fill when empty
    actions.append(f"action = 2 & water > 0 & next(beverage) = beverage & next(water) = water") # fill not empty
    print("    " + " |\n    ".join(actions))