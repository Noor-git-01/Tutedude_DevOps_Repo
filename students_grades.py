
students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

# Add a new student
name = input("Enter student name to add: ")
grade = input("Enter student grade: ").upper()

if name in students:
    print("Student already exists.")
else:
    students[name] = grade
    print("Student added successfully.")

# Update an existing student's grade
name = input("\nEnter student name to update: ")

if name in students:
    grade = input("Enter the new grade: ").upper()
    students[name] = grade
    print("Grade updated successfully.")
else:
    print("Student not found.")

# Display all student grades
print("\nAll Student Grades:")

if students:
    for name, grade in students.items():
        print(name, ":", grade)
else:
    print("No student records found.")
