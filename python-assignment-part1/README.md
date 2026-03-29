# Student Data Parsing & Profile Cleaning

## Overview
This project demonstrates how to clean and transform raw student data into a structured and usable format using Python.

Raw data from real-world sources (forms, spreadsheets, APIs) is often messy. This task focuses on:
- Cleaning inconsistent text data
- Converting data types
- Parsing strings into structured formats
- Validating data integrity

---

## Raw Data Issues

The given dataset contains the following problems:

- **Names** have:
  - Extra spaces
  - Inconsistent casing (uppercase/lowercase)

- **Roll numbers** are stored as **strings** instead of integers

- **Marks** are stored as a **comma-separated string** instead of a list

---

## Objectives

For each student record:

1. **Clean the Name**
   - Remove leading/trailing spaces
   - Convert to Title Case (e.g., `ayesha SHARMA` → `Ayesha Sharma`)

2. **Convert Roll Number**
   - Convert from string → integer

3. **Parse Marks**
   - Convert `"88, 72, 95"` → `[88, 72, 95]`

4. **Validate Name**
   - Ensure each word contains only alphabetic characters
   - Print:
     - ✓ Valid name
     - ✗ Invalid name

5. **Display Output**
   - Print a formatted profile card using f-strings

6. **Special Task**
   - Find student with **Roll No = 103**
   - Print their name in:
     - ALL CAPS
     - lowercase

---

## Technologies Used

- Python 3
- Core concepts:
  - Strings
  - Lists
  - Loops
  - Dictionaries
  - Functions (`map`, `split`, `strip`, `title`)

---

## Code

```python
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = list(map(int, student["marks_str"].split(", ")))

    is_valid = all(word.isalpha() for word in name.split())

    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

    print("✓ Valid name\n" if is_valid else "✗ Invalid name\n")

for student in cleaned_students:
    if student["roll"] == 103:
        print("Name in ALL CAPS :", student["name"].upper())
        print("Name in lowercase:", student["name"].lower())


================================
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
================================
✓ Valid name

...

Name in ALL CAPS : PRIYA NAIR
Name in lowercase: priya nair