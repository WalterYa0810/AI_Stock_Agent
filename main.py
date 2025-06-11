# Step 1: Import your function
from data_fetcher import get_stock_data
from analyzer import analyze_stock
# from data_fetcher import get_stock_data

# Step 2: Call the function with a test symbol
data = get_stock_data("AAPL")
analysis = analyze_stock(data)
# result = get_stock_data("AAPL")

# Step 3: Print the result
print("Stock Data:", data)
print("Analysis:", analysis)
# print(result)
