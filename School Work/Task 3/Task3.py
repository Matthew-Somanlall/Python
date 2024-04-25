
from math import log
from math import isclose

#function 1
def square_root(n:float) -> float:
    est = 5 * (10**((log(n, 10)/2)-1))

    while isclose(est, n) == False:

        est = (est+(n/est))/2

    return est

print(square_root(10))


#function 3
def text_to_braille(l:str) -> str:

    out = ''

    for char  in (l):

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

    return out

print (text_to_braille('abcdefghijklmnopqrstupqrstuvwxyz'))