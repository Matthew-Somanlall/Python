def num_spaces(s:str) -> int:
    '''
    '''
    num_spaces = 0
    for charater in s:
        if charater == ' ':
            num_spaces += 1
    return num_spaces

print(num_spaces("In this example"))