# PG-GPT

A tool that answers questions in Paul Graham's style using GPT-4 and semantic search.

## Setup Instructions

### 1. Set Up a Virtual Environment

It's strongly recommended to use a virtual environment for this project to manage dependencies properly.

#### On Windows:

```bash
# Navigate to project directory
cd PocketFlow-Template-Python

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
# Navigate to project directory
cd PocketFlow-Template-Python

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your terminal prompt indicating that the virtual environment is active.

### 2. Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key

You'll need an OpenAI API key to use this tool:

```bash
# On Windows
set OPENAI_API_KEY=your_api_key_here

# On macOS/Linux
export OPENAI_API_KEY=your_api_key_here
```

For persistent configuration, add this to your environment variables or use a `.env` file.

### 4. Download Paul Graham Essays

Ensure you have a `data` directory with Paul Graham's essays (as .txt files).

### 5. Run the Application

```bash
python main.py
```

## Usage

Once running, you can ask questions and get responses in Paul Graham's writing style:

1. The application will load chunks of Paul Graham's essays
2. Enter your question when prompted
3. The system will find relevant content from the essays
4. A response will be generated in Paul Graham's concise style
5. Type 'exit' to quit

## Features

- Semantic search for finding relevant content
- GPT-4 powered responses in Paul Graham's style
- Formatting to match Paul Graham's concise writing
- Optional web search capability for augmenting responses

## Project Structure

- `main.py`: Main application script
- `utils/`: Utility functions
  - `call_llm.py`: OpenAI API wrapper
  - `process_essays.py`: Essay processing utilities
  - `semantic_search.py`: Vector search functionality
  - `style_formatter.py`: Response formatting utility
  - `duck_search.py`: Web search implementation
  - `web_search.py`: Web search interface

## Troubleshooting

- **"No module named 'openai'"**: Make sure you've activated your virtual environment and installed the requirements
- **API key errors**: Ensure your OpenAI API key is set correctly
- **Memory issues**: If you encounter memory problems, try reducing the number of essay chunks loaded
