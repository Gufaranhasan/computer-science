# Python Data Processing & API Integration Project

## Project Overview

This project is a **production-style Python application** that demonstrates:

* File handling (read/write/append)
* API integration using HTTP requests
* Data processing (filtering, sorting, formatting)
* Robust exception handling
* Logging system with timestamps

The project uses a public API:
https://dummyjson.com (no authentication required)

---

## Project Structure

```
project/
│
├── part3_api_files.py          # Main Python script
├── python_notes.txt            # Generated notes file
├── error_log.txt               # Log file for errors
└── README.md                   # Documentation
```

---

## Task Breakdown

---

## Task 1 — File Read & Write Basics

### Features Implemented

* Created `python_notes.txt` using write mode (`'w'`)
* Appended additional lines using append mode (`'a'`)
* Displayed confirmation messages after each operation

### File Reading

* Reads file line-by-line
* Prints numbered output
* Counts total number of lines
* Performs keyword search (case-insensitive)

### Example Output

```
1. Topic 1: Variables store data...
2. Topic 2: Lists are ordered...
Total lines: 7
```

---

## Task 2 — API Integration

### API Used

Base URL:

```
https://dummyjson.com/products
```

---

### Step 1 — Fetch Products

* Fetches 20 products using GET request
* Parses JSON response
* Displays formatted table:

```
ID | Title | Category | Price | Rating
```

---

### Step 2 — Filter & Sort

* Filters products with rating ≥ 4.5
* Sorts by price (descending)
* Displays filtered list

---

### Step 3 — Category Search

* Fetches all **laptops**
* Prints product name and price

---

### Step 4 — POST Request

* Sends product data to API
* Displays server response

Note: This is a **mock API**, so data is not permanently stored.

---

## Task 3 — Exception Handling

### Part A — Safe Calculator

Function:

```python
safe_divide(a, b)
```

Handles:

* ZeroDivisionError
* TypeError

---

### Part B — Safe File Reader

Function:

```python
read_file_safe(filename)
```

Features:

* Handles missing file errors
* Uses `finally` block
* Ensures graceful execution

---

### Part C — Robust API Calls

All API requests include:

* ConnectionError handling
* Timeout handling
* Generic exception handling

---

### Part D — Input Validation Loop

* Prompts user for product ID (1–100)
* Validates input
* Handles invalid entries
* Fetches product details
* Handles 404 responses gracefully

---

## Task 4 — Logging System

### Features

* Logs errors to `error_log.txt`
* Uses timestamps (`datetime.now()`)
* Appends logs (does not overwrite)

### Log Format

```
[2025-01-15 14:32:01] ERROR in fetch_products: ConnectionError — No connection
```

---

### Test Cases Included

* Simulated ConnectionError (invalid URL)
* Simulated HTTP 404 error (invalid product ID)

---

### Log Output Display

* Reads and prints full log file at end

---

## Technologies Used

* Python 3.x
* Libraries:

  * `requests`
  * `datetime`

---

## Error Handling Strategy

| Error Type        | Handling                |
| ----------------- | ----------------------- |
| ConnectionError   | Network failure message |
| Timeout           | Retry suggestion        |
| HTTP 404          | Handled via status_code |
| FileNotFoundError | Safe fallback           |
| Invalid Input     | Loop validation         |

---

