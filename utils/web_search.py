from typing import List, Dict, Optional
from utils.duck_search import search_with_retry, format_search_results

def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web using DuckDuckGo and return formatted results.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
        
    Returns:
        str: Formatted search results
    """
    results = search_with_retry(query, max_results=max_results)
    return format_search_results(results)

if __name__ == "__main__":
    # Test the search function
    query = input("Enter a search query: ")
    print(f"Searching for: {query}")
    
    results = web_search(query)
    print(results) 