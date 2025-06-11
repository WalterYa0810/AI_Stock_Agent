def analyze_stock(stock_data):
    score = 0
    pe_ratio = stock_data.get("pe_ratio")
    if pe_ratio is not None and pe_ratio <= 30:
        score += 1
    price = stock_data.get("price")
    low_52weeks = stock_data.get("low_52w")
    if price is not None and low_52weeks is not None:
        if price <= low_52weeks * 1.10:
            score += 1
    high_52weeks = stock_data.get("high_52w")
    midpoint = (low_52weeks + high_52weeks) / 2
    if price is not None and midpoint is not None:
        midpoint = (low_52weeks + high_52weeks) / 2
        if price > midpoint:
            score += 1

    if score >= 2:
        suggestion = "Buy"
    elif score == 1:
        suggestion = "Hold"
    else:
        suggestion = "Avoid"

    return {
        "score": score,
        "suggestion": suggestion,
    }