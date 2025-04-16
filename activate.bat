@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Virtual environment activated!
echo.
echo Don't forget to set your OpenAI API key:
echo set OPENAI_API_KEY=your_api_key_here
echo.
echo To run the application:
echo python main.py

cmd /k 