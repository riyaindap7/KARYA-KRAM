@echo off
REM Set the PATH to include the zbarw-20121031\bin folder containing DLLs
set PATH=%CD%\zbarw-20121031\bin;%PATH%

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the main application
python src\connection_own.py
