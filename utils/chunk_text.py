import re
from typing import List

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Break text into semantic chunks, trying to preserve paragraph boundaries.
    
    Args:
        text (str): Input text to be chunked
        chunk_size (int): Target size for each chunk
        overlap (int): Number of characters to overlap between chunks
        
    Returns:
        List[str]: List of text chunks
    """
    # Split text into paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
            
        # If adding this paragraph would exceed chunk_size, start a new chunk
        if current_size + len(paragraph) > chunk_size and current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            # Keep some overlap for context
            if overlap > 0:
                current_chunk = [current_chunk[-1][-overlap:]]
                current_size = len(current_chunk[0])
            else:
                current_chunk = []
                current_size = 0
        
        current_chunk.append(paragraph)
        current_size += len(paragraph)
    
    # Add the last chunk if there's anything left
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks

if __name__ == "__main__":
    # Test the function
    test_text = """
    This is a test paragraph. It contains some text that we want to chunk.
    
    This is another paragraph. It's separate from the first one.
    
    This is a third paragraph that's a bit longer than the others.
    It spans multiple lines but should still be considered one paragraph.
    """
    
    chunks = chunk_text(test_text, chunk_size=50, overlap=10)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("-" * 50) 