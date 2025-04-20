import yfinance
import yfinance as yf
import re

def extract_ticker(text):
    # Basic regex to find tickers (all caps, up to 5 letters)
    match = re.search(r'\b[A-Z]{2,5}\b', text.upper())
    if match:
        return match.group(0)
    return None



def handle_get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        name = stock.info.get("shortName", ticker)

        return f"💹 {name} ({ticker}): ${price:.2f} (latest close)"
    except Exception as e:
        return f"⚠️ Error fetching stock price: {str(e)}"

