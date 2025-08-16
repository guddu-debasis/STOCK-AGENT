📊 Financial Assistant (Stocks & Crypto)

This project is an AI-powered financial assistant built with LangChain and Chainlit.
It helps users fetch stock prices, cryptocurrency prices (BTC), and learn about financial concepts in a conversational way with a sleek web-based UI.

🚀 Features

🔎 Stock Price Lookup

Get historical stock prices for any ticker symbol (e.g., AAPL for Apple).

Special handling for Indian stocks (like Reliance via Yahoo Finance).

Automatic retry with alternative ticker symbols if one fails.

Supports fetching multi-day price summaries.

💰 Crypto Price Lookup

Currently supports Bitcoin (BTC) via CoinGecko API.

Returns real-time USD prices.

🌍 Financial Knowledge Search

Uses Tavily Search to explain general finance concepts (e.g., "What is the stock market?").

Provides human-friendly, clear, and synthesized answers.

💬 Interactive Chat with Chainlit

Talk to your assistant in a chat UI.

History-aware conversation.

Clean, developer-friendly setup.

🛠️ Tech Stack

Python 3

LangChain

Chainlit

Yahoo Finance API (yfinance)

Alpha Vantage API

Tavily Search

📂 Project Structure
.
├── tool_handler.py     # Tools for fetching stock, crypto, and search data
├── prompt_template.py  # Prompt setup for AI assistant instructions
├── .gitignore          # Ignored files (env, cache, etc.)
└── app.py              # Main entrypoint for Chainlit

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone <your-repo-url>
cd <your-repo-name>

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

ALPHA_VANTAGE_API_KEY=your_api_key_here

Then start Chainlit:

chainlit run app.py -w

👉 Open http://localhost:8000 to chat with your assistant.

📖 Example Conversations

![alt text](<Screenshot 2025-08-16 114819.png>)

![alt text](image-1.png)