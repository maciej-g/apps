# -*- coding: utf-8 -*-

try:
    number =  int(input("Please enter an integer greater than zero.[Enter]"))
    if number == 0:
        print("I've got you! You typed ZERO!!!")
    elif number % 2 == 0:
        print(" %s is an even number." %(number))
    elif number % 2 != 0:
        print(" %s is an odd number." %(number))
    else:
        print("An ERROR.")

except ValueError:
    print("Enter an integer!")