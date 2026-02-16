# Student Grade Management System

# Ask for number of students
num_students = int(input("Enter number of students: "))

students = []   # list to store student records
marks_list = [] # list to store marks only

# Function to determine grade
def calculate_grade(marks):
    if marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Input student data
for i in range(num_students):
    print(f"\nStudent {i+1}")
    
    name = input("Enter student name: ")
    
    # Validate marks input
    while True:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks. Please enter between 0 and 100.")
    
    grade = calculate_grade(marks)

    students.append((name, marks, grade))
    marks_list.append(marks)

# Display results
print("\nStudent Results")
print("-------------------")

for student in students:
    print(f"{student[0]} - {student[1]} - Grade {student[2]}")

# Calculate statistics
average_marks = sum(marks_list) / len(marks_list)
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

print("\nClass Statistics")
print("-------------------")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
