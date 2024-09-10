from unit1lesson2 import *

# this was such a tough problem for me so I made use of my notes and overflow to help 
smallest_number = None #by using none i was able to tell the program that i dont know if theres a bigger number then 500 once the program finds a numbre greater then 500 it can replace the none value as it runs the for loop also a way for me to store the value of the smallest number over 500 each time it goes through
thenumbers = number_list

for num in thenumbers:
    if num > 500:
        if smallest_number is None or num < smallest_number: #the condition num < smallest_number makes it so that evrytime it runs we are comparing to a lower number
            smallest_number = num

print("The smallest number greater than 500 is: " + str (smallest_number))
#asnwer is 51