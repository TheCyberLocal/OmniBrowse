from config.config import Config
from utils.fetch_utils import fetch_raw_results
from utils.parse_utils import parse_html

def fetch_results(engine, query, start):
    if engine not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser engine specified")
    raw_html = fetch_raw_results(engine, query)
    results = parse_html(engine, raw_html)
    compiled_results = {i + start: link for i, link in enumerate(results)}
    return compiled_results
