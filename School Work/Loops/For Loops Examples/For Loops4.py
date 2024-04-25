def pi_ish(n:int) -> float:

    # Initialize total to 0 and operator to 1
    total, operator = 0, 1

    for i in range(1, (n), 2):
        total += operator*(4/i)
        operator = operator * -1
    
    # Return the total as a float
    return total

# Print the approximation of pi using the Leibniz formula for pi, with n=10000000
print(pi_ish(10000000))