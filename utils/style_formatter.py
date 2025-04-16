import re
from typing import Optional

def format_response(text: str, max_words: int = 50) -> str:
    """
    Format the response to match Paul Graham's concise style.
    
    Args:
        text (str): Raw response text
        max_words (int): Maximum number of words in the response
        
    Returns:
        str: Formatted response
    """
    # Clean the text
    text = text.strip()
    
    # Remove any markdown formatting
    text = re.sub(r'[*_`]', '', text)
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Keep only the first few sentences that fit within word limit
    formatted_text = []
    word_count = 0
    
    for sentence in sentences:
        words = sentence.split()
        if word_count + len(words) <= max_words:
            formatted_text.append(sentence)
            word_count += len(words)
        else:
            break
    
    # Join sentences and ensure proper punctuation
    result = ' '.join(formatted_text)
    if not result.endswith(('.', '!', '?')):
        result += '.'
    
    return result

if __name__ == "__main__":
    # Test the function
    test_text = """
    In my experience, the most important thing is to find something you're passionate about and work on it relentlessly. 
    Don't worry about what others think. Just focus on creating something meaningful.
    """
    
    formatted = format_response(test_text, max_words=30)
    print("Original text length:", len(test_text.split()))
    print("Formatted text length:", len(formatted.split()))
    print("\nFormatted response:")
    print(formatted) 