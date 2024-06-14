from random import randint

#-----------------------------------------------------------------------------
def get_closest(values, target):
    """
    this takes a list of values and a 
    target value as input, and returns the value 
    in the list that is closest to the target 
    value. 
    """
    # Initialize previous difference to 0
    prev = 0
    
    # Initialize final difference to a large number
    final = float('inf')
    
    # Iterate over the values
    for i in values:
        # Calculate the absolute difference between the current value and the target
        num = abs(i - target)
        
        # If the current difference is less than the previous difference, update the final difference
        if num < prev or prev == 0:
            final = num
        # Update the previous difference
        prev = num
    
    # Return the final difference
    return final


#-----------------------------------------------------------------------------
def get_closest_pair(values1, values2):
    """
    This function finds the closest pair of values between two lists.

    It takes two lists of values as input, `values1` and
    `values2`, and returns a list containing the closest
    pair of values, one from each list.

    The function iterates through the lists, calculates 
    the absolute difference, and keeps track of the minimum 
    difference found. The pair of values with the minimum 
    difference is returned as the closest pair.

    Args:
        values1 (list): The first list of values.
        values2 (list): The second list of values.

    Returns:
        list: A list containing the closest pair of values, one from each list.

    Example:
        values1 = [1, 2, 3, 4, 5]
        values2 = [1.1, 2.2, 3.3, 4.4, 5.5]
        get_closest_pair(values1, values2)
        [1, 1.1]
    """
    # Initialize minimum difference to infinity
    min_diff = float('inf')

    # Initialize closest pair to an empty list
    closest_pair = []

    # Check if both lists have the same length and are not empty
    if len(values1) == len(values2) and values1 != [] and values2 != []:
        # Iterate through the lists using a for loop
        for i in range(len(values1)):
            # Calculate the absolute difference between corresponding elements
            diff = abs(values1[i] - values2[i])
        
            # Check if the current difference is less than the minimum difference found so far
            if diff < min_diff:
                # Update the minimum difference and the closest pair
                min_diff = diff
                closest_pair = [values1[i], values2[i]]

    return closest_pair


#-----------------------------------------------------------------------------
def get_proper_divisors(number):
    """
    Returns a list of proper divisors of a given number in descending order.

    A proper divisor of a number is a divisor that is not the number itself.

    Args:
        number (int): The input number.

    Returns:
        list: A list of proper divisors of the input number in descending order.

    Example:
        get_proper_divisors(12)
        [6, 4, 3, 2, 1]
    """
    num_list = []  # Initialize an empty list to store the divisors
    list_num = number**0.5  # Calculate the square root of the number
    list_num = int(list_num)  # Convert the square root to an integer

    # Iterate from 2 to the square root of the number
    for i in range(2, list_num+1):
        div_num = number / i  # Calculate the division
        if div_num == int(div_num):  # Check if the division is an integer
            num_list.append(i)  # Add the divisor to the list
            if i != div_num:  # Check if it's a perfect square
                num_list.append(int(div_num))  # Add the other divisor to the list

    if number != 1:  # Check if the number is not 1
        num_list.append(1)  # Add 1 to the list of divisors

    num_list.sort()  # Sort the list of divisors
    num_list.reverse()  # Reverse the list to get the divisors in descending order

    return num_list  # Return the list of proper divisors

#-----------------------------------------------------------------------------
def rolling_averages(values, size):
    """
    Calculates the rolling averages of a given list of values.

    Args:
        values (list): The input list of values.
        size (int): The window size for the rolling average.

    Returns:
        list: A list of rolling averages, where each element 
        is the average of the corresponding window of `size` 
        elements in the input list.

    Example:
        values = [1, 2, 3, 4, 5]
        size = 2
        rolling_averages(values, size)
        [1.5, 2.5, 3.5, 4.5]
    """
    output = []  # Initialize an empty list to store the rolling averages

    # Iterate over the input list, starting from the first element and ending at the element before the last `size` elements
    for i in range(len(values)-size+1):
        # Calculate the sum of the current window of `size` elements
        window_sum = sum(values[i:i+size])
        # Calculate the average of the current window
        window_average = window_sum / size
        # Append the average to the output list
        output.append(window_average)

    return output  # Return the list of rolling averages


#-----------------------------------------------------------------------------
def align_strings(strings, substr):

    search_lower = substr.lower()
    processed_strings = []

    # Step 1: Process each string to find and highlight the search string
    for s in strings:
        lower_s = s.lower()
        if search_lower in lower_s:
            index = lower_s.find(search_lower)
            before = s[:index].lower()
            highlight = s[index:index+len(substr)].upper()
            after = s[index+len(substr):].lower()
            processed_strings.append((before + highlight + after, index))

    if not processed_strings:
        return ""

    # Step 2: Find the maximum length of characters before the search string
    max_before_length = max(index for _, index in processed_strings)

    # Step 3: Align each string based on the max_before_length
    aligned_strings = []
    for s, index in processed_strings:
        spaces_needed = max_before_length - index
        aligned_strings.append(' ' * spaces_needed + s)

    # Step 4: Join the processed strings into a single string with each on a new line
    result = "\n".join(aligned_strings)

    return result
#-----------------------------------------------------------------------------
def make_decks(num_decks: int) -> str:
    '''
    Return a list of 2-character cards for num_decks standard card decks,
    ordered by value (A to K) and suit (♠, ♣, ♥, ♦).
    '''
    deck = []
    for c in 'A23456789TJQK':
        for s in '♠♣♥♦':
            deck.extend([f'{c}{s}']*num_decks)
    return deck
#-----------------------------------------------------------------------------
def deal_n_cards(cards, n):
    """
    Deals a specified number of cards from the top of a deck.

    Args:
        cards (list): The input list of cards, representing the deck.
        n (int): The number of cards to deal.

    Returns:
        list: A list of the dealt cards.

    Modifies:
        cards (list): The input list of cards, with the dealt cards removed.

    Example:
        cards = [1, 2, 3, 4, 5]
        n = 2
        dealt_cards = deal_n_cards(cards, n)
        dealt_cards
        [1, 2]
        cards
        [3, 4, 5]
    """
    new_list = cards[0:n]  # Create a new list with the top n cards
    for card in new_list:
        cards.remove(card)  # Remove each dealt card from the original deck

    return new_list  # Return the list of dealt cards


#-----------------------------------------------------------------------------
def cut_the_cards(cards):
    """
    Cuts the deck of cards at a random position.

    Args:
        cards (list): The input list of cards, representing the deck.

    Modifies:
        cards (list): The input list of cards, with the cards rearranged to simulate a cut.

    Example:
        cards = [1, 2, 3, 4, 5]
        cut_the_cards(cards)
        cards
        [3, 4, 5, 1, 2]
    """
    cut_index = randint(1, len(cards)- 1)  # Generate a random index to cut the deck
    bottom_part = cards[:cut_index]  # Split the deck into two parts at the cut index
    top_part = cards[cut_index:]
    cards.clear()  # Clear the original deck
    cards.extend(top_part)  # Add the top part of the deck back to the original deck
    cards.extend(bottom_part)  # Add the bottom part of the deck back to the original deck
    

#-----------------------------------------------------------------------------
def shuffler(values):
    """
    Shuffles a list of values using a custom shuffling algorithm.

    This algorithm is a variation of the riffle shuffle, where the 
    deck is cut into two halves and then merged by repeatedly taking 
    the first card from the left half or the last card from the right half.

    Args:
        values (list): The input list of values to be shuffled.

    Returns:
        list: A new list with the shuffled values.

    Example:
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffled_values = shuffler(values)
        shuffled_values
        [10, 6, 2, 8, 4, 1, 9, 7, 5, 3]
    """
    # Make a copy of the original list to avoid mutation
    cards_copy = values.copy()
    
    # Cut the deck into two halves
    cut_index = len(cards_copy) // 2
    left_half = cards_copy[:cut_index]
    right_half = cards_copy[cut_index:]
    
    # Initialize the new deck
    new_deck = []
    
    # Merge the two halves by repeatedly taking the first card from the left half OR the last card from the right half
    while left_half and right_half:
        coin_flip = randint(1, 2)
        if coin_flip == 1:
            new_deck.append(right_half.pop())
        elif coin_flip == 2:
            new_deck.append(left_half.pop(0))
    
    # Add the remaining cards from the other half to the new deck
    new_deck.extend(left_half)
    new_deck.extend(right_half)
 
    return new_deck

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    '''
    Below is all testing code from the handout's given test cases.
    Uncomment the sets of tests as you complete the functions in order
    to test your own results.
    '''

    #numbers = [5, 9, 0, -3, 15, 8, 4]
    #print(get_closest(numbers, 10))	 
    
    
    #numbers1 = [5, 9, 0, -3, 15, 8, 4]
    #numbers2 = [12, 13, 8, 2, 0, 11, -1]
    #print(get_closest_pair(numbers1, numbers2))
    #print(get_closest_pair(numbers1, [1, 2, 3]))
    
    
    #print(get_proper_divisors(12))
    #print(get_proper_divisors(100))
    #print(get_proper_divisors(29)) 
    #print(get_proper_divisors(1))  
    #print(get_proper_divisors(268435457))
    
    
    #numbers = [3, 9, 2, 10, 14, 20, 13]
    #print(rolling_averages(numbers, 2))	
    #print(rolling_averages(numbers, 4))	 
    #print(rolling_averages(numbers, 10))	 

    
    lines = ["Computer", "Science", "is", "a challenge", "for MANY", "people"]
    print(align_strings(lines, "e"))
    words = ["mathematics", "radius", "theorem", "breathe", "apothem", "area"]
    print(align_strings(words, "The"))
    
    
    #decks = make_decks(1)
    #hand = deal_n_cards(decks, 8)
    #print(len(hand), len(decks))
    #print(hand)
    #print(decks)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cut_the_cards(cards)
    #print(cards) 
    #cut_the_cards(cards)
    #print(cards)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cards = shuffler(cards)
    #print(cards)
    
    
    #cards = ['T♣', 'A♠', '7♥', '4♣', '3♦', 'K♦', 'K♥', '5♣']
    #cards = shuffler(cards)
    #print(cards)
    