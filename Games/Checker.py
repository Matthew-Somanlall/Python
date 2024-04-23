def checker(n:int) -> str:

    string = ''

    for i in range(n):
            
        if n / 2 == int(n / 2):

            if i > 0:
                string += '|\n'
            if i % 2 == 0:
                string += f'{chr(9608)}{chr(9608)}  ' * ( n // 2 )
            else:
                string += f'  {chr(9608)}{chr(9608)}' * ( n // 2 )

        else:
            if i > 0:
                string += '|\n'
            if i % 2 == 0:
                string += f'{chr(9608)}{chr(9608)}  ' * ( n // 2 + 1 )
            else:
                string += f'  {chr(9608)}{chr(9608)}' * ( n // 2  )
                string += '  '


    return string


print (checker(9))

    


