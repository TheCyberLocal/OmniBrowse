from config.config import Config
import requests

def fetch_raw_results(engine, query):
    search_url = Config.SEARCH_ENGINES[engine] + query
    response = requests.get(search_url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch search results")
    return response.content.decode('latin-1')
