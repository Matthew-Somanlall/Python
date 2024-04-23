def checker(n:int) -> str:

    odd = '██  ' * (n // 2)
    even = '  ██' * (n // 2)
    string = ''

    for i in range(n):
            
        if n / 2 == int(n / 2):

            if i % 2 == 0:
                string += f'{odd}|\n'

            else:
                string += f'{even}|\n'

        else:
            if i > 0:
                string += '|\n'
            if i % 2 == 0:
                string += f'{odd}' + f'{chr(9608)}{chr(9608)}'
            else:
                string += f'  {chr(9608)}{chr(9608)}' * ( n // 2 )
                string += '  '


    return string


print (checker(1))

    


