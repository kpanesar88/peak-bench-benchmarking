@echo off
REM Create a virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip to the latest version
pip install --upgrade pip

REM Install required packages from requirements.txt
pip install -r backend\requirements.txt

REM Run your main application (update the path to your app.py as needed)
python backend\app.py

echo Setup complete! Your virtual environment is activated.
echo You can deactivate it using 'deactivate'.
pause
