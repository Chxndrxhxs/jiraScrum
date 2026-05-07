orders = [
    [
        (101, "Laptop", 999.99, 1),
        (102, "Mouse", 25.50, 2),
        (103, "Keyboard", 75.00, 1)
    ],
    [
        (101, "Laptop", 999.99, 2),
        (104, "Monitor", 299.99, 1),
        (105, "Webcam", 89.99, 1)
    ],
    [
        (102, "Mouse", 25.50, 3),
        (103, "Keyboard", 75.00, 2),
        (106, "Headphones", 199.99, 1)
    ]
]

threshold_value = 1000.00

print("Order Totals:")
order_totals = []
for i, order in enumerate(orders, 1):
    total = sum(price * qty for _, _, price, qty in order)
    order_totals.append(total)
    print(f"  Order {i} Total: ${total:.2f}")

most_expensive = max(
    (item for order in orders for item in order),
    key=lambda item: item[2]
)
print(f"\nMost Expensive Item: {most_expensive[1]} (${most_expensive[2]:.2f})")

print("\nProduct Quantity Summary:")
quantity_summary = {}
for order in orders:
    for product_id, name, price, qty in order:
        if product_id not in quantity_summary:
            quantity_summary[product_id] = {"name": name, "total_qty": 0}
        quantity_summary[product_id]["total_qty"] += qty

for product_id, info in quantity_summary.items():
    print(f"  {info['name']}: {info['total_qty']} units")

print(f"\nOrders Exceeding ${threshold_value:.2f}:")
for i, total in enumerate(order_totals, 1):
    if total > threshold_value:
        print(f"  Order {i}: ${total:.2f}")

print("\nUnique Products Ordered:")
unique_products = {}
for order in orders:
    for product_id, name, price, qty in order:
        if product_id not in unique_products:
            unique_products[product_id] = name

for product_id, name in unique_products.items():
    print(f"  {product_id}: {name}")