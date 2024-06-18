from config.config import Config
from utils.fetch_utils import fetch_search_query, fetch_url
from utils.parse_utils import parse_search_query, parse_site_details

def fetch_search_results(engine, query, start_index):
    """
    Fetches search results from a specified search engine.

    Args:
        engine (str): The search engine to use.
        query (str or None): The search query. If None, defaults to 'Latest news about <engine>'.
        start_index (int or None): The starting index for the results. If None, defaults to 1.

    Returns:
        dict: A dictionary of search results keyed by their corresponding rank.

    Raises:
        ValueError: If the specified search engine is invalid.
    """
    # Validate the search engine
    if engine not in Config.SEARCH_ENGINES:
        raise ValueError("Invalid browser engine specified")

    # Set default query if not provided
    query = query if query else f'Latest news about {engine}'

    # Ensure the starting index is positive and set default if not provided
    start_index = abs(start_index or 1)

    # Fetch search results HTML
    search_results_html = fetch_search_query(engine, query)

    # Parse the HTML to extract search results
    search_results_list = parse_search_query(engine, search_results_html)[:5]

    # Compile additional details for each search result
    add_details_to_results(search_results_list)

    # Create a results dictionary with indices starting from the specified start index
    results_dict = {i + start_index: result for i, result in enumerate(search_results_list)}

    return results_dict

def add_details_to_results(results_list):
    """
    Compiles additional details (subtitle and preview image) for each search result.

    Args:
        results_list (list): A list of search result dictionaries containing a 'link'.

    Returns:
        None: The results list is modified in-place.
    """
    for result in results_list:
        # Fetch HTML content of the linked page
        result_link = result["link"]
        result_html = fetch_url(result_link)

        # Parse site details (subtitle and preview image) from the HTML
        site_details = parse_site_details(result_html)

        # Update the result with additional details
        result.update(site_details)
