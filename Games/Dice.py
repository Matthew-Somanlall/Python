from random import randrange

def dice_game(rounds:int) -> str:

    # Initialize variables
    dice_1 = 0
    dice_2 = -1
    point = 0
    string = ''

    # Loop through the specified number of rounds
    for i in range(0, rounds):
        # Generate two random dice rolls
        dice_1 = randrange(1,7)
        dice_2 = randrange(1,7)

        # Check for specific differences between the dice rolls
        if (dice_1 - dice_2 == 1 or dice_1 - dice_2 == -1):
            point += 2

        elif (dice_1 - dice_2 == 4 or dice_1 - dice_2 == -4):
            point += 3

        # Check for a sum of 7
        if (dice_1 + dice_2 == 7):
            point -= 1

        # Check if the dice rolls are the same
        if (dice_1 == dice_2):
            string += f"\n{dice_1},{dice_2}: DONE"
            
        # Turns the current dice rolls and points to the string
        else:
            string += f"\n{dice_1},{dice_2}: {point}"

    # Turns the final points total to the string
    string = f"{string}\n{rounds} rounds: {point} points total"

    # Return the final string
    return string

print(dice_game(100))