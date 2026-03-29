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