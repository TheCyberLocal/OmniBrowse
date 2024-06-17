from config.config import Config
from utils.fetch_utils import fetch_search_query, fetch_url
from utils.parse_utils import parse_search_query, parse_site_details

def fetch_results(engine, query, start):
    if engine not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser engine specified")
    html = fetch_search_query(engine, query)
    results_list = parse_search_query(engine, html)[:5]
    compile_result_details(results_list)
    results_object = {i + start: link for i, link in enumerate(results_list)}
    return results_object

def compile_result_details(results):
    for result in results:
        link = result["link"]
        site_html = fetch_url(link)
        site_details = parse_site_details(site_html)
        result.update(site_details)
