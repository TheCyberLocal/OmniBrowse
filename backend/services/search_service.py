from config.config import Config
from utils.fetch_utils import fetch_search_query
from utils.parse_utils import parse_search_query

def fetch_results(engine, query, start):
    if engine not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser engine specified")
    html = fetch_search_query(engine, query)
    results_list = parse_search_query(engine, html)[:5]
    results_object = {i + start: link for i, link in enumerate(results_list)}
    return results_object
