@echo off
echo Installing Packages...
pip install -r packages.txt
cls
echo Launching...
py app.py
exit