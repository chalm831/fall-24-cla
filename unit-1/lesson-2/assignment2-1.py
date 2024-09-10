from unit1lesson2 import *


smallest_number = number_list[0] 

if number_list[1] < smallest_number:
    smallest_number = number_list[1]

for n in number_list: 
    if n < smallest_number:
        smallest_number = n
        #when I first ran this I forgot to ask it to print the answer for me,
        #so it was really funny to just press and press and nothing would happen until i looked over the notes again

print("the smallest number in this list is: " + str(smallest_number) ) 
#the smallest number is 175
