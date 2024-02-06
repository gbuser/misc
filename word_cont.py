
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def get_data(url):
    r = requests.get(url)
    return r.text

# takes a list of urls and returns aconcatenated string of all "p", "h1" and "h2" text 
def get_text(urls):
    text = ''
    for url in urls:
        data = get_data(url)
        soup = BeautifulSoup(data, 'html.parser')
        tags = ["p", "h1", "h2"]
        for tag in tags:
            for prose in soup.find_all(tag):
                text += prose.get_text() + '\n'
    return text.lower()

# regex patern to extract all words from text, returns list of words
def get_words(text):
    pattern = r'\b[a-z\'-]+\b'
    words = re.findall(pattern, text)
    return words

urls = ["https://www.py4e.com/html3/01-intro",
        "https://www.py4e.com/html3/02-variables",
        "https://www.py4e.com/html3/03-conditional"]
text = get_text(urls)

word_count = Counter(get_words(text))
word_list = [(key, value) for key, value in word_count.items()]
word_list.sort(key = lambda x: x[1], reverse = True)

for words in word_list[:10]:
    print (words)




