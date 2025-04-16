from openai import OpenAI, OpenAIError
from typing import List, Dict, Optional
import os

# Learn more about calling the LLM: https://the-pocket.github.io/PocketFlow/utility_function/llm.html
def call_llm(
    prompt: str,
    context_chunks: Optional[List[str]] = None,
    system_prompt: Optional[str] = None,
    max_tokens: int = 300,
    model: str = "gpt-4"
) -> str:
    """
    Call GPT-4 to generate a response in Paul Graham's style.
    
    Args:
        prompt (str): User's question or prompt
        context_chunks (List[str], optional): Relevant context chunks
        system_prompt (str, optional): System message to guide the model
        max_tokens (int): Maximum number of tokens in response
        model (str): OpenAI model to use
        
    Returns:
        str: Generated response
        
    Raises:
        ValueError: If OpenAI API key is not set
        OpenAIError: If there's an error with the OpenAI API call
    """
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    client = OpenAI()
    
    try:
        # Prepare messages
        messages = []
        
        # Add system message if provided
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Add context if provided
        if context_chunks:
            context = "\n\n".join([f"Context {i+1}:\n{chunk}" for i, chunk in enumerate(context_chunks)])
            messages.append({"role": "user", "content": f"Context:\n{context}\n\nQuestion: {prompt}"})
        else:
            messages.append({"role": "user", "content": prompt})
        
        # Call the API
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=0.9
        )
        
        return response.choices[0].message.content.strip()
        
    except OpenAIError as e:
        print(f"OpenAI API Error: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise

if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    print(call_llm(prompt))
