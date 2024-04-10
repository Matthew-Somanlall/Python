def range_sum(start, end):
    # Swap start and end if start is greater than end

    if start > end:
        start, end = end, start

    # Initialize total to 0
    total = 0

    # Makes range from start to end (inclusive)
    for i in range(start, end+1):

        # Add the current number to total

        total += i

    # Return total
    return total


print(range_sum(5,6))