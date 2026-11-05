# PowerShell Startup Script for Lead Researcher Agent
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Starting Lead Researcher & Outbound Agent" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check if .env exists
if (-not (Test-Path ".env")) {
    if (Test-Path "config\settings.example.json") {
        Write-Host "[INFO] Creating .env from config settings..." -ForegroundColor Yellow
        Set-Content -Path ".env" -Value "GEMINI_API_KEY=YOUR_KEY`nENVIRONMENT=development`nPORT=8000"
    }
}

# 2. Run Pre-flight Tests First
Write-Host "`n[STEP 1/2] Running Pre-flight Validation Tests..." -ForegroundColor Cyan
python -m unittest discover -s tests -v

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[ERROR] Tests failed! Aborting startup to protect production." -ForegroundColor Red
    exit 1
}

Write-Host "`n[STEP 2/2] Launching Agent API Server on http://localhost:8000..." -ForegroundColor Green
python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
