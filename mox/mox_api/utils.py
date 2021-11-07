import requests
from bs4 import BeautifulSoup


def get_title_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.title.text
