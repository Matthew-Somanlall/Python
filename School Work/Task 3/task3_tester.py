from task3_functions import *

MENU = "Test which?\n1. Square Root\n2. Digit Product Sum\n3. Braille\n4. Show All Dominos\n5. Trees\n6. Domino Stack\n7. QUIT\nChoice: "

choice = input(MENU)
while choice != "7":
    
    if choice == "1":
        #-== square_root() ==-
 
        """
        TODO:
        add a validation loop for the input number to make sure it is positive
        """
        number = float(input("Number to square root: "))
        while number < 0:
            print('you are dumb try again')
            number = float(input("Number to square root: "))
        
        
        """
        DO NOT EDIT any code below here for this menu option
        """
        root = square_root(number)
        print(f"Square root of {number} is {root}")
        
        
        
    elif choice == "2":
        #-== digit_product_sum() ==-

        """
        TODO:
        add a validation loop for the number not being negative
        """

        low = int(input("Enter a low number for the range: "))

        high = int(input("Enter a high number for the range: "))

        while low < 0:

            print("you're dumb try again")
            low = int(input("Enter a low number for the range: "))

        while high < 0:
            print("you're dumb try again")
            high = int(input("Enter a high number for the range: "))

        
        """
        TODO:
        add code that will call digit_product_sum() for every number in the
        specified range.  It will determine which number in the range had the
        highest 'digit product sum', and will output that number as well as its
        'digit product sum'
        """
        max_sum = 0
        max_num = 0
        for num in range(low, high + 1):
            sum = digit_product_sum(num)
            if sum > max_sum:
                max_sum = sum
                max_num = num
        print(f"The number with the highest digit product sum in the range [{low}, {high}] is {max_num} with a sum of {max_sum}.")

        
        
            

    elif choice == "3":
        #-== text_to_braille() ==-

        """
        TODO:
        add a validation loop for the menu input being valid (either '1' or '2')
        """
        braille_menu = "\n1. text to Braille\n2. Braille to text\n--> "
        t_to_b_choice = input(braille_menu)

        while (t_to_b_choice != '1') or (t_to_b_choice != '2'):
            print("Invalid input. Please enter '1' or '2'.")
            t_to_b_choice = input(braille_menu)
    
        
        
        """
        DO NOT EDIT any code below here for this menu option
        """
        if t_to_b_choice == '1':
            text = input("Enter text: ")
            braille = text_to_braille(text)
            text = braille_to_text(braille)
            print(f"To Braille: {braille}")
            print(f"Back To Text: {text}")
        else:
            braille = input("Enter Braille: ")
            text = braille_to_text(braille)
            braille = text_to_braille(text)
            print(f"To Text: {text}")
            print(f"Back To Braille: {braille}")
        
        

    elif choice == "4":
        #-== domino_str() ==-
  
        """
        TODO:
        add code that will automatically create and print all possible dominos
        made from numbers 0-6 (inclusive) for each side, resulting in 49
        different dominoes being output (no user input required).
        """
        for i in range (0, 7):
            for j in range (0, 7):
                print(domino_str(i, j))
        
        
        
        
    elif choice == "5":
        #-== tree_box() ==-

        """
        TODO:
        add a validation loop for the size of the tree not being negative
        """
        size = int(input("Tree size: "))
        while size <= 0:
            print("Invalid input. Please enter a positive number")
            size = int(input("Tree size: "))

        """
        DO NOT EDIT any code below here for this menu option
        """
        tree = tree_box(size)
        print(f"Your size-{size} tree:")
        print(tree)
        


    elif choice == "6":
        #-== domino_stack() ==-

        """
        TODO:
        add 3 separate validation loops, validating each input
        value before asking for the next one:
           -for the left number being 1 to 5
           -for the right number being 1 to 5
           -for the target points being positive
        """
        left = int(input("Base domino left # (1 to 5): "))
        while left < 1 or left > 5:
            print("Invalid input. Please enter a number between 1 and 5")
            left = int(input("Base domino left # (1 to 5): "))
        
        
        right = int(input("Base domino right # (1 to 5): "))
        while right < 1 or right > 5:
            print("Invalid input. Please enter a number between 1 and 5")
            right = int(input("Base domino right # (1 to 5): "))

        
        points = int(input("Enter a target number of points: "))
        while points < 0:
            print("Invalid input. Please enter a positive number")
            points = int(input("Enter a target number of points: "))        

        """
        DO NOT EDIT any code below here for this menu option
        """
        results = (domino_stack(left, right, points))
        print(results)

        
    choice = input("\n"+MENU)