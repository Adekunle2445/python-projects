import random
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

while True:
    num_of_dice = input("How many number of Dice (q to quit) :")
    if num_of_dice.capitalize() == "Q":
        print("Thanks for Playing")
        break
    elif not num_of_dice.isdigit():
        print("Only digits allowed")
        continue
    else:
        dice = []
        num_of_dice = int(num_of_dice)
        for num in range(num_of_dice):
            dice.append(random.randint(1, 6))

        print(dice)
        for die in dice:
            for line in dice_art[die]:
                print(line)