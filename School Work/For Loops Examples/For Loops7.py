def times_table(n: int) -> str:

    result = ""

    for i in range(1, n+1):

        for j in range(1, n+1):
            
            result += f"{i * j}\t"
        result += "\n"


    return result

print(times_table(12))