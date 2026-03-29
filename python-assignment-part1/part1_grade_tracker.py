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