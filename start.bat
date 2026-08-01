@echo off
cd /d %~dp0app
echo Starting QueryBase server (model loading ~15s)...
set HF_ENDPOINT=https://hf-mirror.com
start "QueryBase Server" ..\.venv\Scripts\python -m uvicorn main:app --host 127.0.0.1 --port 8000
timeout /t 15 /nobreak >nul
echo Opening browser: http://localhost:8000
start http://localhost:8000
echo.
echo Server is running. Close the "QueryBase Server" window to stop.
pause
