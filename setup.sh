#!/bin/bash

echo "================================================"
echo "PG-GPT Setup Script for Unix/Linux/Mac"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found! Please install Python 3.7+ and add it to your PATH."
    exit 1
fi

# Make the script executable
chmod +x setup.py

# Run the setup script
python3 setup.py

echo ""
echo "================================================"
echo "Setup complete!" 