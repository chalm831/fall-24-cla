import requests
from bs4 import BeautifulSoup

# response = requests.get("https://en.wikipedia.org/wiki/Love") 
response = requests.get("https://medium.com/@taylorchism/what-is-love-d2f697dab911") 

# response = requests.get("https://firebrandmag.com/articles/what-is-love") 
# sucessful and soooo funny 
# response = requests.get("https://www.verywellmind.com/what-is-love-2795343")
# sucess!!!

# response = requests.get("https://www.reddit.com/r/ask/comments/16sv19j/ i_dont_know_what_love_is_can_someone_explain_it/?rdt=39306")
#sigh..reddit comments are dynamically loaded with javascript so the process for scrapping that is a whole other thing. Ignore texts first and second those are failed reddit ones
soup = BeautifulSoup (response.text, "html.parser")
# print(response.body) #just saying like response.body is not valid lol so I looked into how that would actually work, the github scrape text code files were massively helpful 
body = soup.text
# by breaking it down like this I am able to parse through the file first and then get the body tag content and then print it on the terminal because if I just say  print(response.body) it doens't know what you are asking it to print it has no attribute and its not connected
print(body)
# soup = BeautifulSoup(response.text, "html.parser")
all_the_text = soup.get_text()

ns_data = open('fifthscrape.txt', 'w')
ns_data.write(all_the_text)
ns_data.close() 