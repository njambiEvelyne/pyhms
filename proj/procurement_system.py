# procurement_system.py

# List to store purchase requests


# Function to add purchase request
def add_request(request_id, item_name, quantity, department):
    request = {
        "Request ID": request_id,
        "Item Name": item_name,
        "Quantity": quantity,
        "Department": department
    }
    purchase_requests.append(request)
    print("Purchase request added successfully.")

# Function to display all requests
def display_requests():
    print("\nPurchase Requests:")
    for request in purchase_requests:
        print(request)

# Function to search request by ID
def search_request(request_id):
    for request in purchase_requests:
        if request["Request ID"] == request_id:
            print("\nRequest found:", request)
            return
    print("Request not found.")

# Main program
add_request("PR001", "Laptop", 5, "IT Department")
add_request("PR002", "Printer", 2, "Finance Department")

display_requests()

search_request("PR001")