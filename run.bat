REM this is for Windows and it activates the virtual environment and installs modules from requirements.txt
REM run with .\run.bat

@echo off
call myenv\Scripts\activate.bat
pip install -r requirements.txt

