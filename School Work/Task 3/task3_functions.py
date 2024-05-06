
from math import log
from math import isclose
from random import randrange

# Function 1: Calculate the square root of a number
def square_root(n:float) -> float:
    # Initial estimate for the square root, 
    # using the formula 5 * (10^((log(n, 10)/2)-1)) as a rough starting point
    est = 5 * (10**((log(n, 10)/2)-1))

    # Refine the estimate using the Babylonian method, 
    # which is an iterative process that converges on the actual square root
    while isclose(est, n/est) == False:

        est = (est+(n/est))/2

    # Once the estimate has converged, return it as the square root of n
    return est

# Function 2: Calculate the sum of the products of each digit in a number
def digit_product_sum(n:int) -> str:
    # Convert the number to a string to iterate over each digit
    n = str(n)
    total = 0

    # Calculate the product of each digit with every other digit
    for i in (n):
        for j in (n):
            # Multiply the digits and add the product to the total
            total += int(i) * int(j) 

    # Return the total as a string
    return str(total)

# Function 3 pt.1: Convert text to braille
def text_to_braille(l:str) -> str:
    out = ''

    # Iterate over each character in the input string
    for char  in (l):
        # Replace each character with its corresponding braille character
        if char == 'a':
            out += f'\u2801'
        elif char == 'b':
            out += f'\u2803'
        elif char == 'c':
            out += f'\u2809'
        elif char == 'd':
            out += f'\u2819'
        elif char == 'e':
            out += f'\u2811'
        elif char == 'f':
            out += f'\u280b'
        elif char == 'g':
            out += f'\u281b'
        elif char == 'h':
            out += f'\u2813'
        elif char == 'i':
            out += f'\u280a'
        elif char == 'j':
            out += f'\u281a'
        elif char == 'j':
            out += f'\u281a'
        elif char == 'k':
            out += f'\u2805'
        elif char == 'l':
            out += f'\u2807'
        elif char == 'm':
            out += f'\u280d'
        elif char == 'n':
            out += f'\u281d'
        elif char == 'o':
            out += f'\u2815'
        elif char == 'p':
            out += f'\u280f'
        elif char == 'q':
            out += f'\u281f'
        elif char == 'r':
            out += f'\u2817'
        elif char == 's':
            out += f'\u280e'
        elif char == 't':
            out += f'\u281e'
        elif char == 'u':
            out += f'\u2825'
        elif char == 'v':
            out += f'\u2827'
        elif char == 'w':
            out += f'\u283a'
        elif char == 'x':
            out += f'\u282d'
        elif char == 'y':
            out += f'\u283d'
        elif char == 'z':
            out += f'\u2835'
        elif char == ' ':
            out += ' '

    # Return the braille representation of the input string
    return out

# Function 3 pt.2: Convert braille to text
def braille_to_text(l:str) -> str:
    out = ''

    # Iterate over each braille character in the input string
    for char  in (l):
        # Replace each braille character with its corresponding text character
        if '\u2801' == char:
            out += 'a'
        elif '\u2803' == char:
            out += 'b'
        elif '\u2809' == char:
            out += 'c'
        elif '\u2819' == char:
            out += 'd'
        elif '\u2811' == char:
            out += 'e'
        elif '\u280b' == char:
            out += 'f'
        elif '\u281b' == char:
            out += 'g'
        elif '\u2813' == char:
            out += 'h'
        elif '\u280a' == char:
            out += 'i'
        elif '\u281a' == char:
            out += 'j'
        elif '\u281a' == char:
            out += 'j'
        elif '\u2805' == char:
            out += 'k'
        elif '\u2807' == char:
            out += 'l'
        elif '\u280d' == char:
            out += 'm'
        elif '\u281d' == char:
            out += 'n'
        elif '\u2815' == char:
            out += 'o'
        elif '\u280f' == char:
            out += 'p'
        elif '\u281f' == char:
            out += 'q'
        elif '\u2817' == char:
            out += 'r'
        elif '\u280e' == char:
            out += 's'
        elif '\u281e' == char:
            out += 't'
        elif '\u2825' == char:
            out += 'u'
        elif '\u2827' == char:
            out += 'v'
        elif '\u283a' == char:
            out += 'w'
        elif '\u282d' == char:
            out += 'x'
        elif '\u283d' == char:
            out += 'y'
        elif '\u2835' == char:
            out += 'z'
        elif char == ' ':
            out += ' '

    # Return the text representation of the input braille string
    return out

# Function 4: Generate dominoes
def generate_dominoes(i:int ,j:int) -> str:
    right_side = ''

    # Generate the left side of the domino based on the value of j
    if j == 0:
        left_side_1 = f'     |'
        leftside_2 = f'     |'
        leftside_3 = f'     |'
    elif j == 1:
        left_side_1 = f'     |'
        leftside_2 = f'  {chr(9679)}  |'
        leftside_3 = f'     |'
    elif j == 2:
        left_side_1 = f'{chr(9679)}    |'
        leftside_2 = f'     |'
        leftside_3 = f'    {chr(9679)}|'
    elif j == 3:
        left_side_1 = f'{chr(9679)}    |'
        leftside_2 = f'  {chr(9679)}  |'
        leftside_3 = f'    {chr(9679)}|'
    elif j == 4:
        left_side_1 = f'{chr(9679)}   {chr(9679)}|'
        leftside_2 = '     |'
        leftside_3 = f'{chr(9679)}   {chr(9679)}|'
    elif j == 5:
        left_side_1 = f'{chr(9679)}   {chr(9679)}|'
        leftside_2 = f'  {chr(9679)}  |'
        leftside_3 = f'{chr(9679)}   {chr(9679)}|'
    elif j == 6:
        left_side_1 = f'{chr(9679)} {chr(9679)} {chr(9679)}|'
        leftside_2 = '     |'
        leftside_3 = f'{chr(9679)} {chr(9679)} {chr(9679)}|'

    # Generate the right side of the domino based on the value of i
    if i == 0:
        right_side = f'|     |{left_side_1}\n|     |{leftside_2}\n|     |{leftside_3}'
    elif i == 1:
        right_side = f'|     |{left_side_1}\n|  {chr(9679)}  |{leftside_2}\n|     |{leftside_3}'
    elif i == 2:
        right_side = f'|{chr(9679)}    |{left_side_1}\n|     |{leftside_2}\n|    {chr(9679)}|{leftside_3}'
    elif i == 3:
        right_side = f'|{chr(9679)}    |{left_side_1}\n|  {chr(9679)}  |{leftside_2}\n|    {chr(9679)}|{leftside_3}'
    elif i == 4:
        right_side = f'|{chr(9679)}   {chr(9679)}|{left_side_1}\n|     |{leftside_2}\n|{chr(9679)}   {chr(9679)}|{leftside_3}'
    elif i == 5:
        right_side = f'|{chr(9679)}   {chr(9679)}|{left_side_1}\n|  {chr(9679)}  |{leftside_2}\n|{chr(9679)}   {chr(9679)}|{leftside_3}'
    elif i == 6:
        right_side = f'|{chr(9679)} {chr(9679)} {chr(9679)}|{left_side_1}\n|     |{leftside_2}\n|{chr(9679)} {chr(9679)} {chr(9679)}|{leftside_3}'

    # Combine the left and right sides to form the complete domino
    string = f' ___________ \n{right_side}\n ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ '
    
    return string

# Function 5 :Generates a tree in a box
def tree_box(n: int) -> str:
    
    # Initialize variables for the top of the box
    double_slash = '\\'  # This will be used to create the backslashes in the top and bottom of the box
    dash = '-' * (n * 2)  # This will be used to create the horizontal lines in the top and bottom of the box
    string = f'+{dash}+\n'  # This will be the string that represents the box

    # Loop through the rows of the box
    for i in range(1, n+1):
        
        # Initialize variables for the current row
        space = ' ' * (n - i)  # This will be used to create the spaces in the current row
        double_slash = '\\' * i  # This will be used to create the backslashes in the current row
        single_slash = '/' * i  # This will be used to create the forward slashes in the current row
        string += f'|{space}{single_slash}{double_slash}{space}|\n'  # Add the current row to the box string

    # Loop through the rows of the box again to add the even and odd rows
    for i in range(n):
        if i % 2 == 0:
            space = ' ' * (n-1)  # This will be used to create the spaces in the even rows
            even = '|}'  # This will be used to create the even rows
            string += f'|{space}{even}{space}|\n'  # Add the even row to the box string
        else:
            space = ' ' * (n-1)  # This will be used to create the spaces in the odd rows
            odd = '{|'  # This will be used to create the odd rows
            string += f'|{space}{odd}{space}|\n'  # Add the odd row to the box string

    # Add the bottom of the box to the box string
    string += f'+{dash}+'
    
    # Return the box string
    return string

def domino_stack(l: int, r: int, p: int) -> str:

    # Initialize variables for the game
    none = ''  # This will be the return value of the function
    points = 0  # This will be the total points earned in the game
    game = f'\n{generate_dominoes(l,r)}'  # This will be the string that represents the game
    ran_l = randrange(1, 6)  # This will be the random left number for the next domino
    ran_r = randrange(1, 6)  # This will be the random right number for the next domino
    game_num = 1  # This will be the current game number
    g = True  # This will be the flag to continue the game

    # Loop through the game
    while g == True:
        points = 0  # Reset the points for each game
        while (ran_l == l or ran_r == r or ran_l == r or ran_r == l or (ran_l == l and ran_r == r) or (ran_l == r and ran_r == l) == True) and (p > points) == True:
            if ran_l == l or ran_r == r:
                domino = generate_dominoes(ran_l, ran_r)  # Generate the next domino
                game = f'\n{domino + game}'  # Add the next domino to the game string
                points += 2  # Add 2 points for matching the left or right number
            elif ran_l == r or ran_r == l:
                if ran_l == r:
                    domino = generate_dominoes(ran_r,ran_l)  # Generate the next domino
                    game = f'\n{domino + game}'  # Add the next domino to the game string
                    points += 2  # Add 2 points for matching the left or right number
                elif ran_r == l:
                    domino = generate_dominoes(ran_l,ran_r)  # Generate the next domino
                    game = f'\n{domino + game}'  # Add the next domino to the game string
                    points += 2  # Add 2 points for matching the left or right number
            if ran_l == l and ran_r == r or ran_l == r and ran_r == l:
                domino = generate_dominoes(ran_l,ran_r)  # Generate the next domino
                game = f'\n{domino + game}'  # Add the next domino to the game string
                points += 5  # Add 5 points for matching both the left and right numbers
            ran_l = randrange(1, 6)  # Generate a new random left number
            ran_r = randrange(1, 6)  # Generate a new random right number
        print (f'\n{game}')  # Print the current game string
        print(f'Game #{game_num} Points: {points} ')  # Print the current game number and points
        ran_l = randrange(1, 6)  # Generate a new random left number
        ran_r = randrange(1, 6)  # Generate a new random right number
        game_num += 1  # Increment the game number
        if points >= p:  # If the points are greater than or equal to the target points, end the game
            g = False

    return none  # Return the none value

print (domino_stack(1,6,10))