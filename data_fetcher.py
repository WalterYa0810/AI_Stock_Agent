import yfinance as yf
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    name = info.get("shortName")
    price = info.get("currentPrice")
    pe_ratio = info.get("trailingPE")
    low_52w = info.get("fiftyTwoWeekLow")
    high_52w = info.get("fiftyTwoWeekHigh")

    return {
        "name": name,
        "price": price,
        "pe_ratio": pe_ratio,
        "low_52w": low_52w,
        "high_52w": high_52w
    }