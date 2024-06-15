
import requests
from bs4 import BeautifulSoup

def fetch_search_results(url, start):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch search results")

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if 'url?q=' in a['href']]
    results = {i+start+1: link for i, link in enumerate(links[start:start+5])}
    return results
