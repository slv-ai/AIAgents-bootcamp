import requests
from pydantic_ai import Tool

HEADERS = {
            "User-Agent": "WikipediaAgent/1.0 (https://github.com/slv-ai)"
        }
class WikipediaAgent:
    
    SEARCH_URL = "https://en.wikipedia.org/w/api.php"
    PAGE_URL = "https://en.wikipedia.org/w/index.php"
    
    def __init__(self):
        pass
    def search(self, query: str):
        """
        Search Wikipedia for pages matching the query.
    
        Args:
            query: Search term
        
        Returns:
            Dictionary with search results
        """
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query
        }
                
        response= requests.get(self.SEARCH_URL,params=params,headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if not data["query"]["search"]:
            return None
        return [result["title"] for result in data["query"]["search"]]
    def get_page(self, title: str):
        """
        Get the raw content of a Wikipedia page.
    
        Args:
            title: Page title
        
        Returns:
            Raw page content as string
        """
        params = {
            "title": title,
            "action": "raw"
        }
        response = requests.get(self.PAGE_URL, params=params)
        if response.status_code == 404:
            return None
        return response.text

wiki = WikipediaAgent()
def search(query: str) -> list[str]:
    """Search Wikipedia for relevant article titles."""
    return wiki.search(query)

def get_page(title: str) -> str:
    """Retrieve the raw wiki content of a page."""
    return wiki.get_page(title)


