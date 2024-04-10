def frac_sum(n:int) -> float:
    # Initialize total to 0
    total = 0

    for i in range(1, n+1):
        # Add the reciprocal of the current number to total
        total = total + 1/i

    return total

# Print the sum of the reciprocals of the first 50 positive integers
print(frac_sum(50))