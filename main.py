import requests
from bs4 import BeautifulSoup, Comment
from sys import exit
from os import environ

def clean_html(html: str) -> str:
    """
    Remove HTML that will not be used
    """
    soup = BeautifulSoup(html, "html.parser")
    
    for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
        tag.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    # unwrap everything else
    keep = {"a", "button", "h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "ul", "ol"}
    for tag in soup.find_all(True):
        if tag.name not in keep:
            tag.unwrap()
    # remove empty lines and flatten into text
    text = "\n".join([line for line in str(soup).splitlines() if line])
    return text


url = "https://example.com"
response = clean_html(requests.get(url).text)
with open("output.out", "w", encoding="utf-8") as f:
    f.write(response)

def get_sponsors(cleaned_html: str):
    """
    AI chooses whether to advance, quit, or list sponsors
    TODO
    """
    pass


def gather_team_info(number: int) -> dict:
    # will pull from API containing website of team given int
    # TBA api?
    pass


def __init__():
    try:
        team_number = int(input("Enter a FRC team number"))
    except TypeError:
        raise TypeError("Team number (input) must be an integer")
    if 0 < team_number < 10000:
        team_data = gather_team_info(team_number)
        if team_data["website_url"]:
            get_sponsors(team_data["website_url"])
    else:
        raise ValueError("Invalid team number, range = 1 - 9999")