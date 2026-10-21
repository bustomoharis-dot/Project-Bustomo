@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
    py -3 start.py
) else (
    python start.py
)
if errorlevel 1 (
    echo.
    echo Aplikasi belum berjalan. Pastikan Python 3.11+ sudah dipasang.
    pause
)
