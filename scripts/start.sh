#!/usr/bin/env bash
set -e

echo "=========================================="
echo "Starting Lead Researcher & Outbound Agent"
echo "=========================================="

# 1. Run Pre-flight Tests First
echo -e "\n[STEP 1/2] Running Pre-flight Validation Tests..."
python3 -m unittest discover -s tests -v

# 2. Launch FastAPI Service
echo -e "\n[STEP 2/2] Launching Agent API Server on http://0.0.0.0:8000..."
exec python3 -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
