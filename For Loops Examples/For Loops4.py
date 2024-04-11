def pi_ish(n:int) -> float:

    # Initialize total to 0 and operator to 1
    total, operator = 0, 1
    
    # If n is even, minus it by 1
    if isinstance((n/2), int):
        n = n-1

    for i in range(1, (n+1), 2):
        # If operator is 1, add 4/i to total and set operator to -1
        if operator == 1:
            total += (4/i)
            operator = -1
        # If operator is -1, subtract 4/i from total and set operator to 1
        elif operator == -1:
            total -= (4/i)
            operator = 1
    
    # Return the total as a float
    return total

# Print the approximation of pi using the Leibniz formula for pi, with n=10000000
print(pi_ish(10000000))