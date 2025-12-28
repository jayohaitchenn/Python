# loop control

x = "y"
while x == "y":

    # import RNG module

    import random

    # Generate a random number between 1 and 6

    random = random.randint(1, 6)

    # Dice faces

    if random == 1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    
    elif random == 2:
        print("---------")
        print("|       |")
        print("| *   * |")
        print("|       |")
        print("---------")
    
    elif random == 3:
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
    
    elif random == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    
    elif random == 5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    
    elif random == 6:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")

    # ask user if they want to roll again
    
    x = input("Do you want to roll the dice again? (y/n): ")