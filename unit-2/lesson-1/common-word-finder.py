file = open("littlewomen.txt")

word_counts = {}
#at one point i actually switched these two (line 3 values for line 5 values) and if you join me at line 17...
frequent_words  = ["and", "the", "to", "a", "of", "her", "I", "in", "for"]

for line in file:
    for word in line.split():

        if word in frequent_words:
            continue

        if word in word_counts:
            word_counts[word] = word_counts[word] + 1

        else:
            word_counts[word] = 1
#...it kept giving me an error abt not supporting the assignment and that was fixed as soon as i fixed the values for my variables 
allPairs = iter((word_counts.items()))
firstPair = next(allPairs)

mostFrequent = firstPair[0]
print(mostFrequent)
for word in word_counts:
    if word_counts[word] > word_counts[mostFrequent]:
        mostFrequent = word

print("the most frequent word is:", mostFrequent, ",it appears", word_counts[mostFrequent])

#when i first ran it most common was "and"  a total of 7886
#so i made it so that if it was "and" which i put in a lost that it could run over
#i ran it again nect word is "the" a total of 7661 times
#so i added that to the list as we went, the order is reflected in the list 
#more results 3. "to" 5173 times
#4. "a" 4426 times
#5. "of" 3622 times
#6 "her" 2881 times (this was actually my first guess without the program)
#7  "I" 2650 times
#8 "in" 2468 times
#9 "for" 2102 times 
#10 "was" 2016 times

#this was boring so I wondered what would happen if you instead told it to skip words that were less then 3 let letters, its not perfect you do eliminate msybe interesting 2 or 3 letter words but maybe you can skip more boring ones?
#i also experimented by adding image sthat were nt taken in an iphone, some that were developed film transfarred into digital mode, some with a professional camera etc.