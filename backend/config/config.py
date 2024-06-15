
class Config:
    DEBUG = True
    SEARCH_ENGINES = {
        'chrome': 'https://www.google.com/search?q=',
        'edge': 'https://www.bing.com/search?q=',
        'brave': 'https://search.brave.com/search?q=',
        'firefox': 'https://search.yahoo.com/search?p=',
        'duckduckgo': 'https://duckduckgo.com/?q=',
        'ask': 'https://www.ask.com/web?q=',
        'aol': 'https://search.aol.com/search?q='
    }
    SEARCH_DOMAINS = [
        'www.google.com',
        'www.bing.com',
        'search.brave.com',
        'search.yahoo.com',
        'duckduckgo.com',
        'www.ask.com',
        'search.aol.com'
    ]
