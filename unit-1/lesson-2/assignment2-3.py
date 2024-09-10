from unit1lesson2 import *

smallest_even_number = None #again here I tried to use th none value to help me when the program runs the loop
the_numbers = number_list

for x in the_numbers:
    if x % 2 == 0: #i struggle a lot starting code and find editing it to find the right track easier
        if smallest_even_number is None or x < smallest_even_number: #i took a lot from the smallest above 500 algorithim to help guide this one 
            smallest_even_number = x


print("The smallest even number is: " + str (smallest_even_number)) 
#answer is 176
  