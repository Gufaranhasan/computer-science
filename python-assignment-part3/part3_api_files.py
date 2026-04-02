# ===================== IMPORTS =====================
import requests
from datetime import datetime

# ===================== LOGGER =====================
def log_error(context, error_type, message):
    with open("error_log.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ERROR in {context}: {error_type} — {message}\n")


# ===================== TASK 1 =====================
print("\n===== TASK 1: FILE OPERATIONS =====")

# Part A — Write
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")
print("File written successfully.")

# Append
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions improve code reusability.\n")
    f.write("Topic 7: Modules help organize code.\n")
print("Lines appended.")

# Part B — Read
print("\nReading File:")
line_count = 0
lines = []

with open("python_notes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        clean = line.strip()
        print(f"{i}. {clean}")
        lines.append(clean)
        line_count += 1

print("Total lines:", line_count)

# Keyword search
keyword = input("Enter keyword to search: ").lower()
matches = [line for line in lines if keyword in line.lower()]

if matches:
    print("Matching lines:")
    for m in matches:
        print(m)
else:
    print("No matching lines found.")


# ===================== TASK 2 =====================
print("\n===== TASK 2: API INTEGRATION =====")

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        response.raise_for_status()
        data = response.json()["products"]

        print("\nID | Title | Category | Price | Rating")
        print("-" * 60)

        for p in data:
            print(f"{p['id']} | {p['title'][:20]:<20} | {p['category']:<12} | ${p['price']} | {p['rating']}")

        return data

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("fetch_products", "ConnectionError", "No internet")
    except requests.exceptions.Timeout:
        print("Request timed out.")
        log_error("fetch_products", "Timeout", "Server slow")
    except Exception as e:
        print("Unexpected error:", e)
        log_error("fetch_products", "Exception", str(e))

products = fetch_products()

# Filter + Sort
if products:
    filtered = [p for p in products if p["rating"] >= 4.5]
    sorted_products = sorted(filtered, key=lambda x: x["price"], reverse=True)

    print("\nFiltered & Sorted Products:")
    for p in sorted_products:
        print(p["title"], p["price"], p["rating"])

# Category search
def fetch_laptops():
    try:
        response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
        response.raise_for_status()
        data = response.json()["products"]

        print("\nLaptops:")
        for p in data:
            print(p["title"], "-", p["price"])

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("fetch_laptops", "ConnectionError", "No connection")
    except requests.exceptions.Timeout:
        print("Timeout.")
        log_error("fetch_laptops", "Timeout", "Slow response")
    except Exception as e:
        log_error("fetch_laptops", "Exception", str(e))

fetch_laptops()

# POST
def create_product():
    try:
        payload = {
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "A product I created via API"
        }

        response = requests.post(f"{BASE_URL}/add", json=payload, timeout=5)
        print("\nPOST Response:", response.json())

    except Exception as e:
        log_error("create_product", "Exception", str(e))

create_product()


# ===================== TASK 3 =====================
print("\n===== TASK 3: EXCEPTION HANDLING =====")

# Part A
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Part B
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


# Part C & D (Input Loop + Logging)
while True:
    user_input = input("\nEnter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue

    product_id = int(user_input)
    if not (1 <= product_id <= 100):
        print("Out of range.")
        continue

    try:
        response = requests.get(f"{BASE_URL}/{product_id}", timeout=5)

        if response.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", "HTTPError", f"404 for ID {product_id}")
        else:
            data = response.json()
            print(data["title"], "-", data["price"])

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("lookup_product", "ConnectionError", "No internet")
    except requests.exceptions.Timeout:
        print("Timeout.")
        log_error("lookup_product", "Timeout", "Slow response")


# ===================== TASK 4 =====================
print("\n===== TASK 4: LOGGING TEST =====")

# Trigger ConnectionError
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    log_error("test_connection", "ConnectionError", str(e))

# Trigger HTTP error manually
response = requests.get(f"{BASE_URL}/999", timeout=5)
if response.status_code != 200:
    log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")

# Print log file
print("\nError Log Contents:")
with open("error_log.txt", "r", encoding="utf-8") as f:
    print(f.read())