import os
import json

def read_essays(data_dir="./data"):
    """
    Read Paul Graham's essays from the data directory.
    
    Args:
        data_dir (str): Path to the directory containing essay files
        
    Returns:
        dict: Dictionary with filenames as keys and essay content as values
    """
    essays = {}
    
    # Ensure data directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    # Read all .txt files in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    essays[filename] = f.read()
            except Exception as e:
                print(f"Error reading {filename}: {str(e)}")
    
    return essays

if __name__ == "__main__":
    # Test the function
    essays = read_essays()
    print(f"Found {len(essays)} essays")
    for filename, content in essays.items():
        print(f"{filename}: {len(content)} characters") 