
from utils.fetch_utils import fetch_search_results
from config.config import Config

def fetch_results(browser, query, start):
    if browser not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser specified")
    search_url = Config.SEARCH_ENGINES[browser] + query
    results = fetch_search_results(search_url, start)
    return results
