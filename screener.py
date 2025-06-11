from data_fetcher import get_stock_data
from analyzer import analyze_stock
from rationale_generator import generate_rationale
def run_stock_screener(tickers):
    buy_suggestions = []
    for ticker in tickers:
        stock_data = get_stock_data(ticker)
        analysis = analyze_stock(stock_data)
        rationale = generate_rationale(stock_data, analysis)

        if analysis["suggestion"] == "Buy":
            suggestion = {
                "ticker": ticker,
                "score": analysis["score"],
                "suggestion": analysis["suggestion"],
                "rationale": rationale
            }
            buy_suggestions.append(suggestion)

    return buy_suggestions