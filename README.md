
# 📊 STOCK-AGENT

**STOCK-AGENT** is an AI-powered financial assistant built with [Chainlit](https://docs.chainlit.io/) and [LangChain](https://www.langchain.com/).  
It fetches **stock prices, crypto data, and financial knowledge** in a simple, conversational way.


## ✨ Features

📈 **Stock Prices**
  Reliance (India) via **Yahoo Finance**
  Global stocks via **Alpha Vantage API**
  Supports multi-day historical queries (e.g. “Tesla stock price for the last 5 days”)

🪙 **Crypto Prices**
  Currently supports **Bitcoin (BTC)** via **CoinGecko API**

📚 **Finance Knowledge**
  Ask about ETFs, IPOs, or other concepts — uses **Tavily Search** for explanations

🧠 **Conversational Memory**
   Remembers past questions so you can ask follow-ups naturally

⚡ **Powered by LLMs**
  Uses **Google Gemini (`gemini-2.5-flash`)** as the reasoning engine



## 🛠️ Tech Stack

**Chainlit** → Real-time chat UI  
**LangChain** → Agent + tool orchestration  
**Google Gemini** → LLM for reasoning and responses  
**APIs**:
  1.Yahoo Finance (`yfinance`) → Indian stocks  
  2.Alpha Vantage → Global stocks  
  3.CoinGecko → Bitcoin price  
  4.Tavily → Financial knowledge search  



## 📂 Project Structure
```bash
STOCK-AGENT/
├── app.py              
├── tool_handler.py     
├── prompt_template.py  
├── model_setup.py      
├── requirements.txt    
└── README.md

```
## ⚙️ Installation & Setup

### 1. Clone the repo

git clone https://github.com/guddu-debasis/STOCK-AGENT.git
cd STOCK-AGENT


### 2. Create a virtual environment


python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 3. Install dependencies


pip install -r requirements.txt

### 4. Create a `.env` file

Add your API keys in the root directory:

.env
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
GOOGLE_API_KEY=your_google_api_key


* Get Alpha Vantage API key: [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)


* Get Google API key: [https://aistudio.google.com/](https://aistudio.google.com/)

### 5. Run the chatbot

chainlit run app.py -w


Open [http://localhost:8000](http://localhost:8000) in your browser 🎉


## 💬 Example Usage

**User:**
`What is Tesla’s stock price for the last 3 days?`

**Bot:**

On 2025-08-14, TSLA closed at $242.19 USD.
On 2025-08-15, TSLA closed at $239.55 USD.
On 2025-08-16, TSLA closed at $241.72 USD.



## 🚀 Future Improvements

* Support for more cryptocurrencies (ETH, SOL, etc.)
* Smarter ticker lookup and fallbacks
* Chart visualization for stock history
* Portfolio tracking and alerts


