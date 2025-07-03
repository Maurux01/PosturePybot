#!/bin/bash
# Easy deployment script for PosturePybot (Linux)

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Install pip if not present
if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found. Installing pip3..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Install dependencies
pip3 install --user -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies. Please check your Python and pip installation."
    exit 1
fi

# Run the bot
python3 pybot.py 