"""
PG-GPT: A tool to answer questions in Paul Graham's style using GPT-4 and semantic search.
"""

import os
from utils.call_llm import call_llm
from utils.semantic_search import semantic_search
from utils.process_essays import load_chunks
from utils.style_formatter import format_response

def main():
    """Main function to answer questions in Paul Graham's style."""
    # Display a welcome message
    print("=" * 50)
    print("PG-GPT: Paul Graham Style Q&A")
    print("=" * 50)
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ Warning: OPENAI_API_KEY environment variable is not set")
        print("Please set your OpenAI API key to use this tool")
        return
    
    # Load essay chunks
    try:
        chunks = load_chunks()
        print(f"✅ Loaded {len(chunks)} essay chunks")
    except Exception as e:
        print(f"❌ Error loading essay chunks: {e}")
        return
    
    # Interactive Q&A loop
    while True:
        # Get user question
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() in ('exit', 'quit', 'q'):
            break
            
        # Find relevant chunks
        relevant_chunks = semantic_search(question, chunks, top_k=3)
        
        # Generate response
        system_prompt = "You are an AI that answers questions in the style of Paul Graham. Be concise and insightful."
        raw_response = call_llm(
            prompt=question,
            context_chunks=relevant_chunks,
            system_prompt=system_prompt
        )
        
        # Format the response to match Paul Graham's style
        formatted_response = format_response(raw_response)
        
        # Display the response
        print("\nPaul Graham would say:")
        print(formatted_response)
        
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()