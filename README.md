# Conversational AI Stock Assistant
A multi-tool AI agent built with LangChain, Google Gemini, and Chainlit that fetches stock prices, crypto data, and answers complex financial questions.
![alt text](image-1.png)
## Overview
This project is a sophisticated, conversational AI financial assistant. Unlike simple chatbots, this agent can dynamically choose from multiple tools to handle a variety of requests. Whether you need the latest stock price for AAPL, a 5-day history for Amazon, or a definition of "quantitative easing," this assistant can help.
It features a dual-interface system: a simple command-line interface for quick tests and a polished, user-friendly web UI built with Chainlit.
## Features
🤖 Intelligent Agent: Uses a LangChain agent powered by Google Gemini to understand user intent and orchestrate tasks.
🛠️ Dynamic Tool Use: Intelligently selects the right tool for the job, whether it's fetching stock prices, crypto data, or performing a web search.
📈 Multi-Source Stock Data: Fetches stock prices from Alpha Vantage and uses Yahoo Finance as a dedicated source for specific tickers like Indian stocks.
🔍 Smart Ticker Search: Automatically uses Tavily Search to find the correct stock ticker symbol from a company name (e.g., "Apple" -> "AAPL").
🧠 Financial Knowledge Base: Can answer general financial questions and provide definitions by leveraging a web search tool.
💻 Dual Interface: Run it as a classic command-line application (main.py) or as a rich web interface using Chainlit (app.py).
📜 Conversation Memory: Remembers the context of your conversation for natural follow-up questions.
## Tech Stack
Component	Technology
AI Agent	LangChain, Google Gemini (langchain-google-genai)
Stock Data	Alpha Vantage, Yahoo Finance (yfinance)
Crypto Data	CoinGecko API
Web Search	Tavily Search (langchain-tavily)
Web Interface	Chainlit
Environment	Python, python-dotenv
# How It Works
User Input: The user asks a question in the Chainlit UI (e.g., "What was the stock price of Tesla for the last 3 days?").
Agent Brain: The LangChain agent, powered by Google Gemini, receives the input and chat history.
Tool Selection: Based on its instructions, the agent decides which tool to use. In this case, it selects get_stock_price with company_symbol='TSLA' and days=3.
Tool Execution: The tool calls the Alpha Vantage API, retrieves the data, and formats it into a clear summary.
Response Generation: The tool's output is sent back to the agent, which formulates a friendly, human-readable answer.
Memory: The conversation is saved, allowing for contextual follow-ups like "What about Netflix?".
Project Structure
code
## Code
📦 AI-Stock-Assistant
 ┣ 📜 app.py             # Entry point for Chainlit Web UI
 ┣ 📜 main.py            # Entry point for Command-Line Interface
 ┣ 📜 tool_handler.py    # Defines tools (get_stock_price, etc.)
 ┣ 📜 model_setup.py     # Configures the Google Gemini model
 ┣ 📜 prompt_template.py # The core agent prompt and instructions
 ┣ 📜 memory_handler.py  # (Optional) For saving chat history to a file
 ┣ 📜 requirements.txt   # Project dependencies
 ┣ 📜 .env               # API keys (not committed)
 ┗ 📜 README.md          # Project documentation
## Setup and Installation
1️⃣ Clone the Repository
code
Bash
git clone https://github.com/your-username/langchain-stock-chatbot.git
cd langchain-stock-chatbot
2️⃣ Create and Activate a Virtual Environment
code
Bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
code
Bash
pip install -r requirements.txt
4️⃣ Configure API Keys
Create a .env file in the root of the project and add the following keys.
code
Env
# Get from https://makersuite.google.com/app/apikey
GOOGLE_API_KEY="your_google_api_key_here"

# Get from https://www.alphavantage.co/support/#api-key
ALPHA_VANTAGE_API_KEY="your_alpha_vantage_api_key_here"

# Get from https://app.tavily.com/
TAVILY_API_KEY="your_tavily_api_key_here"```

#### 5️⃣ Run the Application

You can run the chatbot in two ways:

**A) With the Chainlit Web Interface (Recommended):**

```bash
chainlit run app.py -w
This will start a local server and open the web UI in your browser.
B) With the Command-Line Interface:
code
Bash
python main.py
Future Improvements
Add graphing/charting of historical stock data.
Integrate financial news sentiment analysis as a tool.
Add support for a wider range of cryptocurrencies.
Create deployment instructions for services like Docker or Streamlit Cloud.