# fast_api
🚀 FastAPI + Gemini AI + Live News Scraper

This project analyzes Indian market sectors using real-time news + Generative AI and produces a Trade Opportunity Report that includes:

📊 Market Overview

🧠 AI-based Opportunity/Risk Analysis

🎯 Final Buy/Sell/Hold Verdict


✨ Features
Feature	Description :

🔍 Live News Extraction	Fetches latest sector news using DuckDuckGo

🤖 AI-Generated Reports	Gemini LLM summarizes and evaluates sector opportunities

🔑 Token-Based Security	Requires Authorization header

🚦 Custom Rate Limiting	5 requests/min per user

⚠ Safe Error Handling	Proper 400 / 401 / 429 responses

⚡ FastAPI Backend	Lightweight & production-ready


🛠 Tech Stack

Python 3

FastAPI

DuckDuckGo Search API

Google Gemini AI

Uvicorn




📁 Project Structure

📦 project
 ┣ 📜 main.py                # FastAPI app + endpoints
 ┣ 📜 ai_analysis.py         # Gemini AI prompt & report generator
 ┣ 📜 data_collector.py      # Live news scraper
 ┣ 📜 requirements.txt       # Dependencies
 ┗ 📜 README.md              # Documentation


⚙️ Setup Instructions
1️⃣ Install dependencies

pip install -r requirements.txt

or manually:

pip install fastapi uvicorn duckduckgo_search google-generativeai

2️⃣ Add Your Gemini API Key

Inside ai_analysis.py

genai.configure(api_key="YOUR_API_KEY")

3️⃣ Run FastAPI Server

uvicorn main:app --reload


Server starts at:
➡ http://127.0.0.1:8000

Docs available at:
➡ http://127.0.0.1:8000/docs


🧪 API Usage
🔹 Endpoint
GET /analyzesector?sector=technology

🔹 Required Header
authorization: your_token

🔹 Example Request
curl -X GET "http://127.0.0.1:8000/analyzesector?sector=energy" \
     -H "authorization: testuser123"

🔹 Example Output
📊 MARKET OVERVIEW
Energy sector gaining momentum due to global demand...

📈 OPPORTUNITIES
 - Renewable growth
 - Electrification drivers

⚠ RISKS
 - Export volatility

🎯 FINAL VERDICT: HOLD

📌 Supported Sectors
[
 "pharmaceuticals",
 "technology",
 "agriculture",
 "energy",
 "finance"
]

🛡 Security & Rate Limit
Check	Behavior
❌ Missing token	Returns 401
❌ Wrong sector	Returns 400
🚦 Too many requests	Returns 429
✔ OK	Runs full analysis

Rate limit definition (inside main.py):
⚠ Max 5 requests / minute per token


🙌 Author
👤 Sarthak Vaghela
 ▪ Python ▪ FastAPI
