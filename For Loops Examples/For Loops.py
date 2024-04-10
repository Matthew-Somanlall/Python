def range_sum(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for i in range(start, end+1):

        total += i

    return total


print(range_sum(5,6))