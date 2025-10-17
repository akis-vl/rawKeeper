@echo off
setlocal

set PYTHON_PATH=py
set SCRIPT_PATH=C:\GIT_Projects\rawKeeper\rawKeeper.py

%PYTHON_PATH% %SCRIPT_PATH% "%cd%"

pause
