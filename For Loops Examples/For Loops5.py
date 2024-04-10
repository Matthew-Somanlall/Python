def num_spaces(s:str) -> int:
    
    # Initialize num_spaces to 0
    num_spaces = 0

    for charater in s:

        # If the current character is a space, increment num_spaces
        if charater == ' ':
            num_spaces += 1

    # Return the number of spaces in the input string
    return num_spaces

# Test the count_spaces function with the string "hello world"
print(num_spaces("Hello World"))