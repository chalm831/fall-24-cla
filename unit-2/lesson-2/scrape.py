# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

fan_response = requests.get("https://www.thesinglesjukebox.com/rosala-bagdad/")
# cla_response = requests.get("https://www.newschool.edu/lang/code-as-a-liberal-art/")
# phil_response = requests.get("https://www.newschool.edu/lang/philosophy/")

# print(response.text[:500])

fan_soup_html = BeautifulSoup(fan_response.text, "html.parser")
# phil_soup_html = BeautifulSoup(phil_response.text, "html.parser")

fan_soup_text = fan_soup_html.get_text()
# phil_soup_text = phil_soup_html.get_text()

fan_data = open('fan.txt', 'w')
fan_data.write(fan_soup_text)
fan_data.close()

# phil_data = open('newschool-phil.txt', 'w')
# phil_data.write(phil_soup_text)
# phil_data.close()


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.body)
      
print("FAN........")
getTitles(fan_soup_html)
# print("Philosophy.........")
# getTitles(phil_soup_html)