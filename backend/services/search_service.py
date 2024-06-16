
from utils.fetch_utils import fetch_unparsed_results, parse_html
from config.config import Config

def fetch_results(engine, query, start):
    if engine not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser engine specified")
    raw_html = fetch_unparsed_results(engine, query)
    print(raw_html)
    links = parse_html(raw_html)
    results = {i + start + 1: link for i, link in enumerate(links[:5])}
    return results
