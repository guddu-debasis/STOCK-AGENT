import os
import json
from datetime import datetime, timedelta
from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
import yfinance as yf
import requests

load_dotenv()

@tool
def get_stock_price(company_symbol: str, days: int = 1) -> str:
    """
    Fetches historical trading data for a stock ticker.
    For Indian stocks (like RELIANCE), uses Yahoo Finance.
    For others (mostly US/global), uses Alpha Vantage.
    Returns a clear, user-friendly multi-day closing price summary.
    """
    upper_symbol = company_symbol.upper()

    try:
        if upper_symbol == "RELIANCE":
         
            ticker = "RELIANCE.NS"
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

            if data.empty:
                return json.dumps({"error": f"No data available for {company_symbol} in the specified date range."})

            results = []
            for date, row in data.iterrows():
                date_str = date.strftime('%Y-%m-%d')
                close_price = row['Close']
                results.append(f"On {date_str}, Reliance Industries Ltd ({upper_symbol}) closed at ₹{close_price:.2f} INR.")

            message = "\n".join(results)
            return json.dumps({"message": message})

        else:
        
            API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
            if not API_KEY:
                return json.dumps({"error": "The Alpha Vantage API key is missing from the .env file."})

            url = "https://www.alphavantage.co/query"
            params = {
                "function": "TIME_SERIES_DAILY",
                "symbol": upper_symbol,
                "apikey": API_KEY,
                "outputsize": "compact"
            }

            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            timeseries = data.get("Time Series (Daily)", {})
            if not timeseries:
                return json.dumps({"error": f"Could not retrieve historical stock price for symbol: {upper_symbol}."})

            today = datetime.now()
            to_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
            from_date = (today - timedelta(days=days)).strftime('%Y-%m-%d')

            current_date = datetime.strptime(to_date, '%Y-%m-%d')
            from_date_dt = datetime.strptime(from_date, '%Y-%m-%d')

            results = []
            while current_date >= from_date_dt:
                date_str = current_date.strftime('%Y-%m-%d')
                if date_str in timeseries:
                    day_data = timeseries[date_str]
                    close_price = day_data["4. close"]
                    results.append(f"On {date_str}, {upper_symbol} closed at ${float(close_price):.2f} USD.")
                current_date -= timedelta(days=1)

            if results:
                message = "\n".join(results)
                return json.dumps({"message": message})
            else:
                return json.dumps({"error": f"No stock data available for symbol: {upper_symbol} in the specified date range."})

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"An API request error occurred: {e}"})
    except Exception as e:
        return json.dumps({"error": f"An unexpected error occurred: {e}"})


@tool
def get_crypto_price(crypto_symbol: str) -> str:
    """
    Fetches the current price of a cryptocurrency in USD using the CoinGecko API.
    Use the symbol 'BTC' for Bitcoin.
    """
    crypto_symbol = crypto_symbol.lower()
    if crypto_symbol != 'btc':
        return json.dumps({"error": f"This tool currently only supports BTC (Bitcoin). Symbol '{crypto_symbol}' is not supported."})

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        price_usd = data.get("bitcoin", {}).get("usd")

        if price_usd is not None:
            crypto_data = {
                "symbol": "BTC",
                "price_usd": price_usd
            }
            return json.dumps(crypto_data)
        else:
            return json.dumps({"error": "Could not parse the price from the API response."})

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"An API request error occurred: {e}"})
    except Exception as e:
        return json.dumps({"error": f"An unexpected error occurred: {e}"})


search = TavilySearch()

tools = [get_stock_price, get_crypto_price, search]
