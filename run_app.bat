@echo off
cd /d "%~dp0"

echo Activating environment...
call automation_env\Scripts\activate

echo Running AI Daily Work Assistant...
python main.py

echo.
echo Done. Press any key to exit.
pause
