import requests
from bs4 import BeautifulSoup

base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")

with open(str(input('Name the file: ')), 'w') as open_file:
    for story_heading in soup.find_all(class_="paywall"):
        if story_heading.a:
            open_file.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            open_file.write(story_heading.contents[0].text.replace("\n", " ").strip())
