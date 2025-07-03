@echo off
REM Easy deployment script for PosturePybot

python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies. Please check your Python and pip installation.
    pause
    exit /b 1
)

python pybot.py
pause 