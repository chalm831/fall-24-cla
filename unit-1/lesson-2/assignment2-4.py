from unit1lesson2 import *

last_alphabet = word_list[0]
#originally here I had an extra line: if word_list[1] > last_alphabet so it kept giving me the first word of the list 
for word in word_list:
    if word > last_alphabet:
         last_alphabet = word

print("the last alphabetical in this list is: " + str(last_alphabet) ) 
#asnwer is violation
