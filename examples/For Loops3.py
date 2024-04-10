def frac_power_sum(n:int) -> float:
    '''
    '''

    total = 0

    for i in range(1, n+1):
        total = total + (1/(2**i))

    return total


print(frac_power_sum(50))
