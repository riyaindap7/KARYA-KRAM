@echo off
REM This script sets up the Python virtual environment and installs required packages

REM Create virtual environment if not exists
if not exist venv (
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install required Python packages
pip install PyQt6 qrcode[pil] opencv-python pyzbar

echo.
echo Setup complete.
echo.
echo IMPORTANT: For pyzbar to work correctly on Windows, you need to install the ZBar DLL dependencies.
echo Please follow these instructions:
echo 1. Download the ZBar Windows binaries from: https://github.com/mchehab/zbar/releases
echo 2. Extract the downloaded archive.
echo 3. Copy the following DLL files to your Python environment's Scripts directory (e.g., venv\Scripts) or to a directory in your system PATH:
echo    - libiconv.dll
echo    - libzbar-64.dll
echo 4. Alternatively, place the DLLs in the same directory as your Python executable or your project root.
echo 5. Restart your terminal or IDE to ensure the DLLs are recognized.
echo.
echo After completing these steps, you should be able to run your project without errors.
echo.
echo To activate the virtual environment later, run:
echo call venv\Scripts\activate.bat
echo.
echo To run the project, use:
echo python src\connection_own.py
