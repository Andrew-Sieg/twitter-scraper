REM This is for Windows and it activates the virtual environment and installs modules from requirements.txt
REM Run with .\run.bat

if not exist myenv\Scripts\activate.bat (
    python -m venv myenv
)
call myenv\Scripts\activate.bat
pip install -r requirements.txt


