import os #at first i actually forgot to put the text file within the corpus folder so this was added later so i could do that
import markovify

folder_path = "corpus"
text = ""

for filename in os.listdir(folder_path):
    file_path = os.path.join (folder_path, filename)
    with open(file_path) as f:
     text += f.read() 
#this operates much in the same way I dicussed in my previous project main diffrence is the last line where I am using with to assign teh file i am opneing to the variable f. as the program reads my code it will take the text variable I had set as empty to itirate through the loop as that file in that folder.
# text = open("love.txt").read()
# i used this originally before i realized i had to put the text inside of a folder 

#the code kept breaking because the text wasn't viable. I realized this bc i tried a randome book text file and then it did work. I had to edit my love.txt file a bit add more too. scrape more. Then it started working.
#next step I felt was to start messing around because while it was producing kind of beautiful stuff I needed it to not just be 105 words and to see how I could chnage the structure
generator = markovify.Text(text, state_size=2)
#what is the state size how does that affect it? this part is the ammount of words the text will consider when predicting the next word. 1 gave these like very poetic sonet like sentences, longer gave more cohesion ut less variety?


paragraph = ""

for i in range(30): #this is the number of sentences 
    paragraph += str(generator.make_short_sentence(70)) #maximum character length of each sentence by messing with these i could fullfill word count but also 
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")