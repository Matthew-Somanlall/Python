def frac_power_sum(n:int) -> float:
    # This function calculates the sum of the
    # reciprocals of 2 raised to the power of i,
    # where i ranges from 1 to n (inclusive).

    # Initialize total to 0
    total = 0

    for i in range(1, n+1):
        # Add the reciprocal of 2 raised to the power of i to total
        total = total + (1/(2**i))

    # Return the total as a float
    return total

# Print the sum of the reciprocals of 2 raised to the power of i, where i ranges from 1 to 50 (inclusive)
print(frac_power_sum(50))
