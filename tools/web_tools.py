import requests

def search_web(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    return requests.get(url).text[:3000]