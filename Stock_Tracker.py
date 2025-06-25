stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "RIL": 1431,
    "HDFC": 3840,
    "AIRTEL": 1856,
    "ICICI": 1417,
    "INFOSYS": 1612,
    "ITC": 417,
    "L&T": 3610,
    "TCS": 3506,
    "SBI": 793,
    "SUN PHARMA": 1678,
    "ORACLE": 9709,
    "MPHASIS": 2701,
    "HCL": 1726,
    "HAL": 5057,
    "WIPRO": 261,
    "DLF": 857,
    "ADANI": 992,
    "ONGC": 254,
    "EICHER": 5370,
    "BOSCH": 32240
}

portfolio = {}

while True:
    stock = input("Enter stock symbol or 'Done': ").strip().upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ STOCK NOT FOUND")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = quantity

# Display final portfolio
total_value = 0
print("\n📊 YOUR STOCK PORTFOLIO\n")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\n💰 Total Portfolio Value: ${total_value}")

# Ask to save
choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("📈 Stock Portfolio Summary\n\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\n💰 Total Portfolio Value: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'.")
else:
    print("❌ Portfolio not saved.")