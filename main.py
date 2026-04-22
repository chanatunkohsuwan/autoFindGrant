import asyncio
import os
import re
import requests
from bs4 import BeautifulSoup, Comment
from sys import exit
from os import environ
from mistralai.client import Mistral
from mistralai.client.models import UserMessage

from dotenv import load_dotenv

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
mistral_client = Mistral(api_key=MISTRAL_API_KEY)

def clean_html(html: str) -> str:
    """
    Remove HTML that will not be used
    """
    soup = BeautifulSoup(html, "html.parser")
    
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


url = "https://example.com"
response = clean_html(requests.get(url).text)
def find_sponsor_page(soup: BeautifulSoup):
    # simple soup search for now but will add more complicated filtering if needed
    return [a.get('href') for a in soup.find_all('a', href=True)]

url = "https://frc5190.org/sponsors/"

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
page = clean_soup(soup)

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
    f.write(page)

async def request_chat_completion(messages, retries=5):
    try:
        response = mistral_client.chat.complete_async(
            model="mistral-large-latest",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        if retries != 0:
            return await request_chat_completion(messages, retries=retries-1)
        else:
            raise(e)
        
async def main():
    print("hello world")

if __name__ == "__main__":
    asyncio.run(main())