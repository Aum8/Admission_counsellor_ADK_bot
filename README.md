# 🎓 Admissions Counselor Agent

A voice-enabled AI agent that answers prospective student queries about university courses, durations, and fees using Google ADK.

## Features
- Answers course queries from Excel data
- Handles follow-up questions about durations/fees
- Gracefully escalates unknown questions
- Simple web interface

## 🚀 Quick Start
1. **Install requirements**:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r reequirements.txt
   ```

2. **Create a .env file**:
   ```bash
   GOOGLE_API_KEY=

   #Only if you want to deploy on google cloud
   GOOGLE_GENAI_USE_VERTEXAI=1
   GOOGLE_CLOUD_PROJECT= #Your Project ID
   GOOGLE_CLOUD_LOCATION=asia-south1-a
   ```

3. **Start the bot**:
   ```bash
   adk web
    ```

**Thats it! The bot is now available on http://localhost:8000**
