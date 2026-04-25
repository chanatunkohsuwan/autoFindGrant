# look at the upload.py, lets try to get all that info to load
# ima try to organize the methods here to be in order of what will be called in main.py 
# or just have core higher up and utilities/fallbacks lower

import asyncio
import json
import os
import dotenv
import re
import requests
from bs4 import BeautifulSoup, Comment
from sys import exit
from mistralai.client import Mistral
from mistralai.client.models import UserMessage

import upload
from upload import Team

dotenv.load_dotenv()
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
BLUE_ALLIANCE_API_KEY = os.environ.get("BLUE_ALLIANCE_API_KEY")

mistral_client = Mistral(api_key=MISTRAL_API_KEY)

with open("prompts.json", "r") as f:
    prompts = json.load(f)


def gather_team_info(team_number: int) -> dict:
    team_key = f"frc{team_number}"
    url = f"https://www.thebluealliance.com/api/v3/team/{team_key}"
    headers = {
        "X-TBA-Auth-Key": BLUE_ALLIANCE_API_KEY
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    json_response = json.loads(response.json)
    team = Team()
    team.id = json_response.id
    team.name = json_response.name
    


def fetch_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def clean_soup(soup: BeautifulSoup) -> str:
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


def search_sponsor_page_url(soup: BeautifulSoup) -> str:
    # simple soup search for now but will add more complicated filtering if needed
    urls = [a.get('href') for a in soup.find_all('a', href=True)]
    if len(urls) == 0:
        return
    else:
        return urls[0]


def get_sponsors(url: str, tries=10):
    # run the function recursively to search the webpage
    html = fetch_html(url)
    if html == None:
        return
    soup = BeautifulSoup(html, "html.parser")
    sponsor_url = search_sponsor_page_url()
    if sponsor_url == None:
        text = clean_soup(soup)
        # call ai
        messages = [
            {
                "role": "system",
                "content": prompts["navigation"]
            },
        ]
        # TODO: call the ai and set up tools and recursive navigation


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


if __name__ == "__main__":
    # write whatever tests here.
    
    
    
    
    pass

