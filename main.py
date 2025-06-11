import pandas as pd
import urllib.request
from screener import run_stock_screener

# Pull S&P 500 tickers from Wikipedia using a user-agent header
def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    tables = pd.read_html(response.read())
    df = tables[0]
    return df["Symbol"].tolist()

# Step 1: Get the tickers
tickers = get_sp500_tickers()
tickers = tickers[:50]  # Optional: limit to top 50 for faster testing

# Step 2: Run the screener
suggestions = run_stock_screener(tickers)

# Step 3: Display results
for s in suggestions:
    print(f"✅ BUY: {s['ticker']} (Score: {s['score']})")
    print(f"Reason: {s['rationale']}\n")
