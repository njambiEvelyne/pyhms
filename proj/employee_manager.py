# employee_manager.py

# List to store employees
employees = []

# Function to add employee
def add_employee(emp_id, name, salary):
    employee = {
        "id": emp_id,
        "name": name,
        "salary": salary
    }
    employees.append(employee)
    print("Employee added successfully.")

# Function to display employees
def display_employees():
    print("\nEmployee List:")
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Salary: {emp['salary']}")

# Main program
add_employee("E001", "John", 50000)
add_employee("E002", "Mary", 60000)

display_employees()