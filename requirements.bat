@echo off
echo Installing required Python packages...
python -m pip install --upgrade pip
python -m pip install pillow requests
python -m pip install pyinstaller
echo ✅ Packages installed.
pause