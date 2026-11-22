@echo off
rem Double-click to refresh the GitHub profile 30-day activity card.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0refresh-stats.ps1" %*
echo.
pause
