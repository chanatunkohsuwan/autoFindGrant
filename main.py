import re
import requests
from bs4 import BeautifulSoup, Comment

def clean_soup(soup: BeautifulSoup):
    # remove useless html filler slop
    for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
        tag.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    # unwrap everything else
    keep = {"a", "button", "img", "h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "ul", "ol"}
    for tag in soup.find_all(True):
        if tag.name not in keep:
            tag.unwrap()
    # remove empty lines and flatten into text
    text = "\n".join([line for line in str(soup).splitlines() if line])
    return text

def find_sponsor_page(soup: BeautifulSoup):
    # simple soup search for now but will add more complicated filtering if needed
    return [a.get('href') for a in soup.find_all('a', href=True)]

url = "https://frc5190.org/sponsors/"

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
page = clean_soup(soup)

with open("output.out", "w", encoding="utf-8") as f:
    f.write(page)