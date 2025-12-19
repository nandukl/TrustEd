@echo off
echo Starting TrustEd - Smart Fake Degree Recognition System
echo.

echo Starting Backend Server...
start "Backend" /D "backend" cmd /k "python -m uvicorn main:app --reload"

timeout /t 5 /nobreak >nul

echo Starting Frontend Server...
start "Frontend" /D "frontend" cmd /k "npm run dev"

echo.
echo Servers started successfully!
echo Frontend URL: http://localhost:5173
echo Backend API: http://localhost:8000
echo Backend Docs: http://localhost:8000/docs
echo.
echo Press any key to exit...
pause >nul