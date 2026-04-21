import requests
from bs4 import BeautifulSoup

def clean_html(html):
    # remove useless html filler slop
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    # remove empty lines
    text = "\n".join([line for line in text.splitlines() if line.strip()])
    return text

url = "https://frc5190.com"

response = clean_html(requests.get(url).text)

with open("output.out", "w", encoding="utf-8") as f:
    f.write(response)