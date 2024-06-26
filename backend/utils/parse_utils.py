from config.config import Config
from bs4 import BeautifulSoup
import urllib.parse
import re


def parse_site_details(html):
    soup = BeautifulSoup(html, 'html.parser')

    subtitle = ''
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        text = paragraph.get_text().strip()
        if text and "Your browser is not supported." not in text:
            subtitle += text + ' '
            if len(subtitle) > Config.SUBTITLE_LENGTH:
                subtitle = subtitle[:Config.SUBTITLE_LENGTH]
                subtitle = subtitle[:subtitle.rfind(' ')]
                subtitle += '...'
                break

    return { 'subtitle': subtitle }

def parse_search_query(engine, html):
    if engine == 'google':
        return parse_google_search(html)

def parse_href_for_link(raw_href):
    # Negated Character Parsing
    # http or https and one or more characters, not including (?&#:@"').
    url_match = re.search(r'https?:\/\/[^\s?&#:@"\\]+', raw_href)

    if url_match:
        # Extract the matched URL
        encoded_url = url_match.group()
        # Decode the URL after successful match
        return urllib.parse.unquote(encoded_url)
    else:
        return None

def parse_google_search(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # Find all <a> tags
    a_tags = soup.find_all('a', href=True)

    for a in a_tags:
        # Check if there is an <h3> element inside the <a> tag
        h3 = a.find('h3')
        if h3:
            # Extract the href attribute from the <a> tag
            a_tag_href = a['href']
            link = parse_href_for_link(a_tag_href)
            # Extract the text within the <div> inside the <h3> element
            div = h3.find('div')
            if div:
                title = div.get_text()

                if link and title:
                    results.append({ "title": title, "link": link })

    return results
