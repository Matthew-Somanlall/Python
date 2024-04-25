
from math import log
from math import isclose

#function 1
def square_root(n:float) -> float:
    est = 5 * (10**((log(n, 10)/2)-1))

    while isclose(est, n) == False:
        print("/")
        est = (est+(n/est))/2

    return est
print(".")
print (square_root(10))


#function 3
def text_to_braille(l:str) -> str:

    out = ''

    for char  in (l):

        if char == 'a':
            out += f'\u2801'
        elif char == 'b':
            out += f'\u2803'

    return out

print (text_to_braille('a'))