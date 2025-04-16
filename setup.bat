@echo off
echo ================================================
echo PG-GPT Setup Script for Windows
echo ================================================
echo.

REM Check if Python is installed
python --version > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python not found! Please install Python 3.7+ and add it to your PATH.
    goto :end
)

REM Run the setup script
python setup.py

:end
echo.
echo ================================================
echo Press any key to exit...
pause > NUL 