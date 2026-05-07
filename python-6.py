transactions = [
    ("AAPL", "BUY",  100, 150.00, "2023-01-15"),
    ("GOOGL", "BUY",  50, 2800.00, "2023-01-20"),
    ("AAPL", "BUY",   50, 160.00, "2023-02-10"),
    ("MSFT", "BUY",   75, 300.00, "2023-02-15"),
    ("AAPL", "SELL",  75, 170.00, "2023-03-05"),
    ("GOOGL", "SELL", 20, 2900.00, "2023-03-10"),
    ("TSLA", "BUY",   40, 800.00, "2023-03-15"),
    ("MSFT", "SELL",  25, 320.00, "2023-04-01"),
    ("TSLA", "SELL",  15, 750.00, "2023-04-10"),
    ("AAPL", "BUY",   25, 155.00, "2023-04-15"),
]

current_prices = {
    "AAPL": 175.00,
    "GOOGL": 2850.00,
    "MSFT": 310.00,
    "TSLA": 780.00,
}

stocks = {}
for symbol, t_type, qty, price, date in transactions:
    if symbol not in stocks:
        stocks[symbol] = {
            "shares": 0,
            "total_invested": 0.0,
            "realized_pnl": 0.0,
            "volume": 0,
            "buy_queue": []          
        }

    s = stocks[symbol]
    s["volume"] += qty

    if t_type == "BUY":
        s["shares"] += qty
        s["total_invested"] += qty * price
        s["buy_queue"].append((qty, price))

    elif t_type == "SELL":
        shares_to_sell = qty
        cost_of_sold = 0.0
        while shares_to_sell > 0 and s["buy_queue"]:
            lot_qty, lot_price = s["buy_queue"][0]
            take = min(shares_to_sell, lot_qty)
            cost_of_sold += take * lot_price
            shares_to_sell -= take
            if take == lot_qty:
                s["buy_queue"].pop(0)
            else:
                s["buy_queue"][0] = (lot_qty - take, lot_price)

        s["realized_pnl"] += (qty * price) - cost_of_sold
        s["shares"] -= qty
        s["total_invested"] -= cost_of_sold

print("Current Portfolio Holdings:")
for symbol, s in stocks.items():
    print(f"  {symbol}: {s['shares']} shares")

print("\nStock Performance Analysis:")
for symbol, s in stocks.items():
    current_value   = s["shares"] * current_prices[symbol]
    unrealized_pnl  = current_value - s["total_invested"]
    total_pnl       = s["realized_pnl"] + unrealized_pnl

    s["current_value"]  = current_value
    s["unrealized_pnl"] = unrealized_pnl
    s["total_pnl"]      = total_pnl

    print(f"\n  {symbol}:")
    print(f"    - Total Investment : ${s['total_invested']:.2f}")
    print(f"    - Current Value    : ${current_value:.2f}")
    print(f"    - Realized P&L     : ${s['realized_pnl']:.2f}")
    print(f"    - Unrealized P&L   : ${unrealized_pnl:.2f}")
    print(f"    - Total P&L        : ${total_pnl:.2f}")

best  = max(stocks.items(), key=lambda x: x[1]["total_pnl"])
worst = min(stocks.items(), key=lambda x: x[1]["total_pnl"])
print(f"\nBest Performing Stock : {best[0]} (+${best[1]['total_pnl']:.2f})")
print(f"Worst Performing Stock: {worst[0]} (-${abs(worst[1]['total_pnl']):.2f})")

total_invested      = sum(s["total_invested"]  for s in stocks.values())
total_current_value = sum(s["current_value"]   for s in stocks.values())
total_realized      = sum(s["realized_pnl"]    for s in stocks.values())
total_unrealized    = sum(s["unrealized_pnl"]  for s in stocks.values())
overall_pnl         = total_realized + total_unrealized
return_pct          = (overall_pnl / total_invested) * 100

print(f"""
Portfolio Summary:
  Total Investment      : ${total_invested:.2f}
  Current Portfolio Value: ${total_current_value:.2f}
  Total Realized P&L    : ${total_realized:.2f}
  Total Unrealized P&L  : ${total_unrealized:.2f}
  Overall P&L           : ${overall_pnl:.2f}
  Return Percentage     : {return_pct:.2f}%""")

print("\nTrading Volume (Total Shares Traded):")
sorted_by_volume = sorted(stocks.items(), key=lambda x: x[1]["volume"], reverse=True)
for symbol, s in sorted_by_volume:
    print(f"  {symbol}: {s['volume']} shares")