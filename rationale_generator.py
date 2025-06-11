def generate_rationale(stock_data, analysis):
    stock_name = stock_data.get("name")
    suggestion = analysis.get("suggestion")

    reason = ""
    if suggestion == "Buy":
        reason += f"{stock_name} is a good buy right now."
    elif suggestion == "Hold":
        reason += f"{stock_name} may be good to hold right now."
    else:
        reason += f"{stock_name} is not recommended to buy right now."

    pe_ratio = stock_data.get("pe_ratio")
    price = stock_data.get("price")
    low_52weeks = stock_data.get("low_52w")
    high_52weeks = stock_data.get("high_52w")

    if pe_ratio is not None:
        if pe_ratio > 30:
            reason += " Its P/E ratio is above 30, suggesting the stock may be overvalued."
        else:
            reason += " Its P/E ratio is at or below 30, indicating a fair or undervalued price."

    if price is not None and low_52weeks is not None:
        if price <= low_52weeks * 1.10:
            reason += " The stock is currently trading near its 52-week low, which may signal a potential buying opportunity."
        else:
            reason += " The stock is trading well above its 52-week low, suggesting a higher entry price."

    if price is not None and low_52weeks is not None and high_52weeks is not None:
        midpoint = (low_52weeks + high_52weeks) / 2
        if price > midpoint:
            reason += " The price is above the midpoint of its 52-week range, indicating possible upward momentum."
        else:
            reason += " The price is below the midpoint of its 52-week range, which could indicate underperformance or value."

    return reason
