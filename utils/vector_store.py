import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dimension: int):
        """
        Initialize a vector store with FAISS index.
        
        Args:
            dimension (int): Dimension of the vectors to be stored
        """
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []
    
    def create_index(self, chunks: List[str], embeddings: List[List[float]]) -> None:
        """
        Create or update the FAISS index with new chunks and embeddings.
        
        Args:
            chunks (List[str]): List of text chunks
            embeddings (List[List[float]]): List of corresponding embeddings
        """
        if not chunks or not embeddings:
            raise ValueError("Chunks and embeddings cannot be empty")
        
        if len(chunks) != len(embeddings):
            raise ValueError("Number of chunks must match number of embeddings")
        
        # Convert embeddings to numpy array
        embeddings_array = np.array(embeddings).astype('float32')
        
        # Add to FAISS index
        self.index.add(embeddings_array)
        
        # Store chunks
        self.chunks.extend(chunks)
    
    def search_index(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Search the index for most similar chunks.
        
        Args:
            query_embedding (List[float]): Query embedding vector
            top_k (int): Number of results to return
            
        Returns:
            List[Tuple[str, float]]: List of (chunk, distance) tuples
        """
        if not self.chunks:
            raise ValueError("Index is empty")
        
        # Convert query embedding to numpy array
        query_array = np.array([query_embedding]).astype('float32')
        
        # Search
        distances, indices = self.index.search(query_array, top_k)
        
        # Return results
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.chunks):  # Ensure index is valid
                results.append((self.chunks[idx], float(distances[0][i])))
        
        return results

if __name__ == "__main__":
    # Test the vector store
    from get_embedding import get_embedding, get_embeddings
    
    # Create some test data
    test_chunks = [
        "This is the first test chunk.",
        "This is the second test chunk.",
        "This is the third test chunk."
    ]
    
    # Get embeddings
    embeddings = get_embeddings(test_chunks)
    dimension = len(embeddings[0])
    
    # Create and populate vector store
    store = VectorStore(dimension)
    store.create_index(test_chunks, embeddings)
    
    # Test search
    query = "Find the first chunk"
    query_embedding = get_embedding(query)
    results = store.search_index(query_embedding, top_k=2)
    
    print("Search results:")
    for chunk, distance in results:
        print(f"Distance: {distance:.4f}")
        print(f"Chunk: {chunk}")
        print("-" * 50) 