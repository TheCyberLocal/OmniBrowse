from config.config import Config
import urllib.parse
import requests
import re

def fetch_unparsed_results(engine, query):
    search_url = Config.SEARCH_ENGINES[engine] + query
    response = requests.get(search_url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch search results")
    return response.content.decode('latin-1')


def parse_html(html):
    # Negated Character Parsing
    # http or https and one or more characters, not including (?&#:@"').
    url_pattern = re.compile(r'https?:\/{2}[^\s?&#:@"\\]+')

    # Matched Character Parsing
    # http or https and one or more A-Z, a-z, 0-9, or the five symbols (./%-_).
    # url_pattern = re.compile(r'https?:\/{2}[\w\.\-\%\/]+')

    decoded_urls = []
    seen_second_domains = set()
    for encoded_url in url_pattern.findall(html):
        decoded_url = urllib.parse.unquote(encoded_url)

        # https://www.google.com/search
        # ['https:', '','www.google.com', 'search']
        domain = decoded_url.split('/')[2]

        #     www    .     google   .    com
        # {subdomain}.{second-level}.{top-level}
        #   interview   .    io
        # {second-level}.{top-level}
        if domain.count('.') == 1:
            second_domain = domain[:domain.find('.')]
        else:
            second_domain = domain[domain.find('.') + 1:domain.rfind('.')]

        if second_domain not in seen_second_domains:
            decoded_urls.append(decoded_url)
            seen_second_domains.add(second_domain)

    return decoded_urls
