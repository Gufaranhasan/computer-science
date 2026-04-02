# Restaurant Management System (Python)

## Project Overview

This project is a **Python-based Restaurant Management System** that simulates real-world restaurant operations including:

* Menu display and analysis
* Customer order processing (cart system)
* Inventory management with reorder alerts
* Daily sales tracking and analysis

It is designed to demonstrate **core Python concepts** such as dictionaries, lists, loops, functions, and data analysis.

---

## Dataset Description

### 1. Menu

Contains item details:

* Category (Starters, Mains, Desserts)
* Price
* Availability status

### 2. Inventory

Tracks:

* Stock levels
* Reorder thresholds

### 3. Sales Log

Stores daily orders with:

* Order ID
* Items purchased
* Total bill amount

---

## Tasks

### Task 1: Menu Management

* Displays menu grouped by category
* Calculates:

  * Total number of items
  * Available items
  * Most expensive item
  * Items priced below ₹150

---

### Task 2: Cart & Order System

* Add items to cart (with validation)
* Remove items from cart
* Update item quantity
* Prevent duplicate entries
* Handle:

  * Non-existent items
  * Unavailable items
* Generate final bill with:

  * Subtotal
  * GST (5%)
  * Total payable amount

---

###  Task 3: Inventory Management

* Uses **deep copy** to protect original inventory
* Simulates stock deduction after order placement
* Handles insufficient stock scenarios
* Generates **Reorder Alerts** when stock falls below threshold

---

### Task 4: Sales Analysis

* Calculates **daily revenue**
* Identifies **best-selling day**
* Finds **most ordered item**
* Updates sales log dynamically
* Displays all orders using enumeration

---

## Sample Output

* Menu grouped by category
* Cart updates after each operation
* Final order summary with GST
* Inventory changes and reorder alerts
* Daily revenue report and best day
* Numbered list of all orders

---