def number_trapezoids(n:int) -> int:
    
    out = ''
    m = n * 10 / n

    for i in range(1, int(m + 1)):

        out += f'/{n * i}\\'

    return out

print(number_trapezoids(12))