from math import log
from math import isclose
import math
import random

def matthew (n):
    est = 5 * (10**((log(n, 10)/2)-1))

    while isclose(est, n/est) == False:

        est = (est+(n/est))/2

    return est

def ron (number):
    estimate = 5*10**(math.log(number,10)/2 - 1)
    while math.isclose((number/estimate),estimate) == False:
        estimate = (estimate + (number/estimate))/2
    return estimate

n=100

num_1 = matthew(n)
num_2 = ron(n)

i = 0

while i < 100:
    i += 1
    n = 34534
    num_1 = matthew(n)
    num_2 = ron(n)
    if num_1 == num_2:
        print ('true')
    else:
        print ('flase')