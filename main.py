import requests
from bs4 import BeautifulSoup

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
        tag.decompose()
    return soup.get_text(separator="\n")

url = "https://frc5190.com"

response = clean_html(requests.get(url).text)

with open("output.out", "w", encoding="utf-8") as f:
    f.write(response)