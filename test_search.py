"""
Test script for the web search functionality
"""

from utils.web_search import web_search
import sys

def main():
    """Test the web search functionality."""
    print("=" * 50)
    print("Web Search Tool Test")
    print("=" * 50)
    
    # Get search query from command line or use default
    query = sys.argv[1] if len(sys.argv) > 1 else "Paul Graham essays Lisp programming"
    
    print(f"Searching for: {query}")
    print("=" * 50)
    
    try:
        results = web_search(query)
        print(results)
        print("Search completed successfully!")
    except Exception as e:
        print(f"Error during search: {e}")
        import traceback
        traceback.print_exc()
    
if __name__ == "__main__":
    main() 