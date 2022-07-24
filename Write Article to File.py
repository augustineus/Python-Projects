#change base_url to the site you want to scrape
#change text_to_find's class_='' to the HTML class of the site
#this will return a text file with many lists, all with one string containing the text of the HTML class(es) chosen

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.theguardian.com/us'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

filename = input('Save file as: ')

with open(filename, 'w') as f:
    for text_to_find in soup.find_all(class_="u-faux-block-link__overlay js-headline-text"):
        newSoup = str(text_to_find.contents)
        f.write(''.join(newSoup))