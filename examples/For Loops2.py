def frac_sum(n):
    '''
    '''
    
    total = 0
    denominator = 1

    for i in range(1, n):
        total = total + 1/denominator
        denominator+=1
    
    return total


print(frac_sum(50))