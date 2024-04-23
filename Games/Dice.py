from random import randrange

def dice_game(rounds:int) -> str:

    dice_1 = 0
    dice_2 = -1
    point = 0
    string = ''

    for i in range(0, rounds):
        #while dice_1 != dice_2:
        
        dice_1 = randrange(1,7)
        dice_2 = randrange(1,7)

        if (dice_1 - dice_2 == 1 or dice_1 - dice_2 == -1):
            point += 2

        elif (dice_1 - dice_2 == 4 or dice_1 - dice_2 == -4):
            point += 3

        if (dice_1 + dice_2 == 7):
            point -= 1

        if (dice_1 == dice_2):
            string += f"\n{dice_1},{dice_2}: DONE"
            
        else:
            string += f"\n{dice_1},{dice_2}: {point}"

    string = f"{string}\n{rounds} rounds: {point} points total"

    return string

print(dice_game(100))