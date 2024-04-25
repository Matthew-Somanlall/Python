from random import randrange

spins = 0
above = 'Above 25:'
below = 'Below 25:'
highest = 0
count = 0

while spins != 25:

    count += 1

    spins = randrange(0,50)

    if spins > 25:
        below += f'{spins},'

    elif spins < 25:
        above += f'{spins},'

    if highest < spins:
        highest = spins

print(f"It took {count} spins to get a 25.")
print(f"{above}")
print(f"{below}")
print(f"Highest overall spin was a {highest}.")
