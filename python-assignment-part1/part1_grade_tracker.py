raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()
    
    # Convert roll to integer
    roll = int(student["roll"])
    
    # Convert marks_str to list of integers
    marks = list(map(int, student["marks_str"].split(", ")))
    
    # Validate name (only alphabets in each word)
    is_valid = all(word.isalpha() for word in name.split())
    
    # Store cleaned data
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    
    # Print profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")
    
    # Print validation result
    if is_valid:
        print("✓ Valid name\n")
    else:
        print("✗ Invalid name\n")

# Find student with roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print("Name in ALL CAPS :", student["name"].upper())
        print("Name in lowercase:", student["name"].lower())

       # Initial data
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# Function to assign grade
def get_grade(score):
    if 90 <= score <= 100:
        return "A+"
    elif 80 <= score <= 89:
        return "A"
    elif 70 <= score <= 79:
        return "B"
    elif 60 <= score <= 69:
        return "C"
    else:
        return "F"

print(f"\nStudent: {student_name}")
print("\n--- Subject-wise Performance ---")

# Using for loop
for sub, mark in zip(subjects, marks):
    grade = get_grade(mark)
    print(f"{sub:10} : {mark} ({grade})")

# Calculations
total = sum(marks)
average = round(total / len(marks), 2)

# Highest and lowest
max_mark = max(marks)
min_mark = min(marks)

max_subject = subjects[marks.index(max_mark)]
min_subject = subjects[marks.index(min_mark)]

print("\n--- Summary ---")
print(f"Total Marks   : {total}")
print(f"Average Marks : {average}")
print(f"Highest       : {max_subject} ({max_mark})")
print(f"Lowest        : {min_subject} ({min_mark})")

# While loop for adding new subjects
new_count = 0

print("\n--- Add New Subjects (type 'done' to stop) ---")

while True:
    new_subject = input("Enter subject name: ").strip()
    
    if new_subject.lower() == "done":
        break
    
    mark_input = input(f"Enter marks for {new_subject}: ").strip()
    
    # Validation
    if not mark_input.isdigit():
        print("⚠️ Invalid input! Marks must be a number.\n")
        continue
    
    mark = int(mark_input)
    
    if mark < 0 or mark > 100:
        print("⚠️ Marks must be between 0 and 100.\n")
        continue
    
    # Add valid data
    subjects.append(new_subject)
    marks.append(mark)
    new_count += 1
    print("✓ Added successfully!\n")

# Updated calculations
updated_average = round(sum(marks) / len(marks), 2)

print("\n--- Final Summary ---")
print(f"New Subjects Added : {new_count}")
print(f"Updated Average    : {updated_average}") 

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []
topper_name = ""
topper_avg = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)
    
    status = "Pass" if avg >= 60 else "Fail"
    
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
    
    # Track topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    print(f"{name:<18} | {avg:>7.2f} | {status}")

# Class average
class_avg = round(sum(averages) / len(averages), 2)

print("\n--- Summary ---")
print(f"Passed Students : {pass_count}")
print(f"Failed Students : {fail_count}")
print(f"Class Topper    : {topper_name} ({topper_avg})")
print(f"Class Average   : {class_avg}")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)
print()

# Step 2: Convert to Title Case
title_case = clean_essay.title()
print("2. Title Case:")
print(title_case)
print()

# Step 3: Count occurrences of "python"
count_python = clean_essay.count("python")
print("3. Count of 'python':", count_python)
print()

# Step 4: Replace "python" with "Python 🐍"
replaced_text = clean_essay.replace("python", "Python 🐍")
print("4. Replaced Text:")
print(replaced_text)
print()

# Step 5: Split into sentences
sentences = clean_essay.split(". ")
print("5. Sentences List:")
print(sentences)
print()

# Step 6: Print numbered sentences
print("6. Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")