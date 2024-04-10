def frac_sum(n:int) -> float:
    '''
    '''
    
    total = 0

    for i in range(1, n+1):
        total = total + 1/i

    return total


print(frac_sum(50))