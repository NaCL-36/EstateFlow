@echo off
REM EstateFlow Startup Script for Windows

echo.
echo =========================================
echo       EstateFlow - Real Estate Platform
echo =========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    py -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install/upgrade dependencies
echo Installing dependencies...
pip install -q -r requirements.txt
echo.

REM Run Flask app
echo.
echo =========================================
echo Starting EstateFlow...
echo =========================================
echo.
echo Website URL: http://localhost:5000
echo Admin URL:  http://localhost:5000/admin/login
echo Username:   admin
echo Password:   admin123
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
