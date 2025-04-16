import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
from typing import List, Dict, Optional

def search_duckduckgo(query: str, max_results: int = 5, timeout: int = 10) -> List[Dict[str, str]]:
    """
    Search DuckDuckGo and return search results.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
        timeout (int): Request timeout in seconds
        
    Returns:
        List[Dict[str, str]]: List of dictionaries containing 'title', 'url', and 'snippet'
    """
    # Encode the query for URL
    encoded_query = urllib.parse.quote_plus(query)
    
    # DuckDuckGo search URL
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
    
    # Set headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://duckduckgo.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Make the request
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find search results
        results = []
        for result in soup.select('.result'):
            # Extract result data
            title_element = result.select_one('.result__title')
            link_element = result.select_one('.result__url')
            snippet_element = result.select_one('.result__snippet')
            
            if title_element and link_element:
                title = title_element.get_text(strip=True)
                # DuckDuckGo HTML results often have relative links that need to be parsed
                href = link_element.get('href', '')
                if href.startswith('/'):
                    parsed_url = urllib.parse.urlparse(href)
                    query_params = urllib.parse.parse_qs(parsed_url.query)
                    url = query_params.get('uddg', [''])[0]
                else:
                    url = href
                
                snippet = snippet_element.get_text(strip=True) if snippet_element else ""
                
                results.append({
                    'title': title,
                    'url': url,
                    'snippet': snippet
                })
                
                if len(results) >= max_results:
                    break
        
        return results
    
    except requests.exceptions.RequestException as e:
        print(f"Error during search request: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def search_with_retry(query: str, max_retries: int = 3, delay: int = 2, **kwargs) -> List[Dict[str, str]]:
    """
    Search with retry logic to handle temporary failures.
    
    Args:
        query (str): The search query
        max_retries (int): Maximum number of retry attempts
        delay (int): Delay between retries in seconds
        **kwargs: Additional arguments to pass to search_duckduckgo
        
    Returns:
        List[Dict[str, str]]: Search results
    """
    for attempt in range(max_retries):
        try:
            results = search_duckduckgo(query, **kwargs)
            if results:
                return results
        except Exception as e:
            print(f"Search attempt {attempt + 1} failed: {e}")
        
        if attempt < max_retries - 1:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
            # Increase delay for next attempt (exponential backoff)
            delay *= 2
    
    print("All search attempts failed")
    return []

def format_search_results(results: List[Dict[str, str]]) -> str:
    """
    Format search results into a readable string.
    
    Args:
        results (List[Dict[str, str]]): List of search result dictionaries
        
    Returns:
        str: Formatted search results
    """
    if not results:
        return "No results found."
    
    formatted = "Search Results:\n\n"
    for i, result in enumerate(results, 1):
        formatted += f"{i}. {result['title']}\n"
        formatted += f"   URL: {result['url']}\n"
        formatted += f"   {result['snippet']}\n\n"
    
    return formatted

if __name__ == "__main__":
    # Test the search function
    query = "OpenAI GPT-4 models"
    print(f"Searching for: {query}")
    
    results = search_with_retry(query)
    print(format_search_results(results)) 