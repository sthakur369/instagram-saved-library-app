@echo off
setlocal enabledelayedexpansion
title Instagram Saved Library
cd /d "%~dp0"

:: 1. Check if Python is installed
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 app.py
    goto :eof
)

where python >nul 2>nul
if %errorlevel%==0 (
    python app.py
    goto :eof
)

where python3 >nul 2>nul
if %errorlevel%==0 (
    python3 app.py
    goto :eof
)

:: 2. Fallback if Python is not installed: Open browser directly
echo.
echo ========================================================
echo   Instagram Saved Library - Browser Mode
echo ========================================================
echo.
echo   Python was not detected on your system.
echo   Opening the app in direct browser mode...
echo.
start "" "public\index.html"
echo   [Tip] To use the background local server, install Python 3.10+
echo   from https://www.python.org or Microsoft Store.
echo.
pause
