@echo off
REM Create a virtual environment named venv
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install PyQt6
pip install PyQt6

echo Virtual environment setup complete. To activate it later, run:
echo call venv\Scripts\activate.bat
