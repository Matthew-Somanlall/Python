from random import randint

#-----------------------------------------------------------------------------
def get_closest(values, target):

    """
    """

    prev = 0

    for i in values():

        num = i - target
        num = abs(num)
        if num < prev:
            final = num
        if prev < num:
            final = prev

    return final


#-----------------------------------------------------------------------------
def get_closest_pair(values1, values2):

    """
    """
    
    min_diff = float('inf')
    closest_pair = []
    
    if len(values1) == len(values2) and values1 != [] and values2 != []:
        for i in range(len(values1)):
            diff = abs(values1[i] - values2[i])
            if diff < min_diff:
                min_diff = diff
                closest_pair = [values1[i], values2[i]]

    return closest_pair


#-----------------------------------------------------------------------------
def get_proper_divisors(number):

    """
    example: 72 sqr it
    [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36]
    [1, 2, 36, 3, 24, 4, 18, 6, 12, 8, 9]

    example: 100
    [1, 2, 50, 4, 25, 5, 20, 10]
    """
    
    num_list =[]

    for i in range(2, ((number//2)+1)):
        div_num = number / i
        if div_num == int(div_num):
            num_list.append(int(div_num))

    if number != 1:
        num_list.append(1)

    return num_list

#-----------------------------------------------------------------------------
def rolling_averages(values, size):
    
    """
    """

    output = []

    for i in range(len(values)-size+1):
        output.append(sum(values[i:i+size])/size)

    return output


#-----------------------------------------------------------------------------
def align_strings(strings, substr):


    return []


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

    new_list = cards[0:n]
    for card in new_list:
        cards.remove(card)

    return new_list


#-----------------------------------------------------------------------------
def cut_the_cards(cards):

    """
    """

    cut_index = randint(1, len(cards)- 1)
    bottom_part = cards[:cut_index]
    top_part = cards[cut_index:]
    cards.clear()
    cards.extend(top_part)
    cards.extend(bottom_part)
    

#-----------------------------------------------------------------------------
def shuffler(values):
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
    
    
    print(get_proper_divisors(12))
    print(get_proper_divisors(29)) 
    print(get_proper_divisors(268435457))
    
    
    #numbers = [3, 9, 2, 10, 14, 20, 13]
    #print(rolling_averages(numbers, 2))	
    #print(rolling_averages(numbers, 4))	 
    #print(rolling_averages(numbers, 10))	 

    
    #lines = ["Computer", "Science", "is", "a challenge", "for MANY", "people"]
    #print(align_strings(lines, "e"))
    #words = ["mathematics", "radius", "theorem", "breathe", "apothem", "area"]
    #print(align_strings(words, "The"))
    
    
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
    