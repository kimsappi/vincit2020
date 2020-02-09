#!/bin/sh
cd frontend
npm run build
cd ..
python3 backend/app.py
