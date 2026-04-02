# ===================== DATA =====================
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# ===================== TASK 1 =====================
print("\n========== FULL MENU ==========")
categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"\n===== {category} =====")
    for name, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:<15} ₹{details['price']:.2f}   [{status}]")

# Stats
total_items = len(menu)
available_items = sum(1 for item in menu.values() if item["available"])
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
under_150 = [(name, d["price"]) for name, d in menu.items() if d["price"] < 150]

print("\nMenu Stats:")
print("Total items:", total_items)
print("Available items:", available_items)
print(f"Most expensive: {most_expensive[0]} ₹{most_expensive[1]['price']}")
print("Items under ₹150:")
for name, price in under_150:
    print(f"{name} ₹{price}")

# ===================== TASK 2 =====================
cart = []

def add_item(item_name, qty):
    if item_name not in menu:
        print(f"{item_name} does not exist.")
        return
    if not menu[item_name]["available"]:
        print(f"{item_name} is unavailable.")
        return
    
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += qty
            return
    
    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })

def remove_item(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            return
    print(f"{item_name} not in cart.")

def update_quantity(item_name, qty):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = qty
            return
    print(f"{item_name} not found.")

def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)

# Simulation
add_item("Paneer Tikka", 2)
print_cart()

add_item("Gulab Jamun", 1)
print_cart()

add_item("Paneer Tikka", 1)
print_cart()

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
print_cart()

# Order Summary
print("\n========== Order Summary ==========")
subtotal = 0

for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:<15} x{item['quantity']}    ₹{total:.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("------------------------------------")
print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total_payable:.2f}")
print("====================================")

# ===================== TASK 3 =====================
import copy

inventory_backup = copy.deepcopy(inventory)

# Modify inventory
inventory["Paneer Tikka"]["stock"] = 999

print("\nInventory (Modified):", inventory["Paneer Tikka"])
print("Inventory Backup:", inventory_backup["Paneer Tikka"])

# Restore
inventory = copy.deepcopy(inventory_backup)

# Deduct stock
for item in cart:
    name = item["item"]
    qty = item["quantity"]
    stock = inventory[name]["stock"]

    if stock < qty:
        print(f"Warning: Only {stock} available for {name}")
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= qty

# Reorder alerts
print("\nReorder Alerts:")
for name, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

print("\nFinal Inventory:", inventory)
print("\nBackup Inventory:", inventory_backup)

# ===================== TASK 4 =====================
print("\nRevenue Per Day:")
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(date, "₹", total)

best_day = max(daily_revenue, key=daily_revenue.get)
print("\nBest Selling Day:", best_day)

# Most ordered item
from collections import Counter

counter = Counter()
for orders in sales_log.values():
    for order in orders:
        counter.update(order["items"])

print("Most Ordered Item:", counter.most_common(1)[0])

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue Per Day:")
daily_revenue = {}
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(date, "₹", total)

best_day = max(daily_revenue, key=daily_revenue.get)
print("\nUpdated Best Selling Day:", best_day)

# Enumerate orders
print("\nAll Orders:")
count = 1
for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1
        