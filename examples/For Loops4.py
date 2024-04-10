def pi_ish(n:int) -> float:
    '''
    '''

    total = 0
    operator = 1
    if isinstance((n/2), int):
        n = n-1

    for i in range(1, (n+1), 2):
        if operator == 1:
            total = total + (4/i)
            operator = -1
        elif operator == -1:
            total = total - (4/i)
            operator = 1
    return total

print(pi_ish(10000000))
