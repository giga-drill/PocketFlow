from openai import OpenAI
import numpy as np
from typing import List

def get_embedding(text: str, model: str = "text-embedding-3-small") -> List[float]:
    """
    Get embedding for a text using OpenAI's embedding API.
    
    Args:
        text (str): Input text to embed
        model (str): OpenAI embedding model to use
        
    Returns:
        List[float]: Vector embedding of the text
    """
    client = OpenAI()
    
    # Clean and prepare text
    text = text.strip()
    if not text:
        raise ValueError("Text cannot be empty")
    
    # Get embedding
    response = client.embeddings.create(
        input=text,
        model=model
    )
    
    return response.data[0].embedding

def get_embeddings(texts: List[str], model: str = "text-embedding-3-small") -> List[List[float]]:
    """
    Get embeddings for multiple texts using OpenAI's embedding API.
    
    Args:
        texts (List[str]): List of texts to embed
        model (str): OpenAI embedding model to use
        
    Returns:
        List[List[float]]: List of vector embeddings
    """
    client = OpenAI()
    
    # Clean and prepare texts
    texts = [text.strip() for text in texts if text.strip()]
    if not texts:
        raise ValueError("No valid texts provided")
    
    # Get embeddings
    response = client.embeddings.create(
        input=texts,
        model=model
    )
    
    return [data.embedding for data in response.data]

if __name__ == "__main__":
    # Test the function
    test_text = "This is a test sentence for embedding."
    embedding = get_embedding(test_text)
    print(f"Embedding dimension: {len(embedding)}")
    print(f"First few values: {embedding[:5]}")
    
    # Test batch embedding
    test_texts = ["First test sentence.", "Second test sentence."]
    embeddings = get_embeddings(test_texts)
    print(f"Number of embeddings: {len(embeddings)}")
    print(f"First embedding dimension: {len(embeddings[0])}") 