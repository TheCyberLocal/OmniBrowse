import requests
from bs4 import BeautifulSoup
from config.config import Config
import urllib.parse

def fetch_search_results(url, start):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch search results")

    soup = BeautifulSoup(response.text, 'html.parser')
    raw_links = [urllib.parse.unquote(a['href']).split('/url?q=')[1] for a in soup.find_all('a', href=True) if 'url?q=' in a['href']]
    links = []
    seen_domains = set()

    engine_domains = Config.SEARCH_DOMAINS  # Add more if needed

    for link in raw_links:
        if link.startswith('http') or link.startswith('https'):
            full_url = link.split('&sa=')[0]
        else:
            full_url = urllib.parse.urljoin(url, link)

        parsed_url = urllib.parse.urlparse(full_url)
        domain = parsed_url.netloc

        if domain not in seen_domains and domain not in engine_domains:
            links.append(full_url)
            seen_domains.add(domain)

    results = {i + start + 1: link for i, link in enumerate(links[start:start + 5])}
    return results
