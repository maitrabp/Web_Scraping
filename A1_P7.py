from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import re

url = "https://www.maitrapatel.info"

xml_data = requests.get(url).content
scrapped_data = BeautifulSoup(xml_data, 'html.parser')

tagCount = {}

for tag in scrapped_data.find_all(True):
    if tagCount.__contains__(tag.name):
        tagCount[tag.name] = tagCount[tag.name] + 1
    else:
        tagCount[tag.name] = 1
print("Tags from SCRAPPED URL--> ", url)
for key, value in tagCount.items():
    print(key, "--> ", value)
