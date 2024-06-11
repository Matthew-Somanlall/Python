from random import randrange

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

    return []


#-----------------------------------------------------------------------------
def align_strings(strings, substr):
    return ""


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
    return []


#-----------------------------------------------------------------------------
def cut_the_cards(cards):
    return None
    

#-----------------------------------------------------------------------------
def shuffler(values):
    return []




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
    #print(get_proper_divisors(29)) 
    #print(get_proper_divisors(268435457))
    
    
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
    