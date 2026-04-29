@echo off
REM Weekly AI Deployment Newsletter - Scheduled Task
REM Runs: scrape all sources -> analyze with Claude -> generate report -> send email

cd /d "C:\Users\alexa\OneDrive\Documents\GSB\claude\ai-deployment-monitor"

REM Set UTF-8 encoding for Rich console output
chcp 65001 >nul 2>&1
set PYTHONIOENCODING=utf-8

REM Run the full newsletter pipeline
python main.py newsletter --type executive --to alexandroskalivas1@gmail.com

REM Log completion
echo [%date% %time%] Newsletter pipeline completed >> newsletter_log.txt
