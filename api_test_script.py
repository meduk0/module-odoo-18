import requests
import json

# Configuration
BASE_URL = "http://localhost:8069"
HEADERS = {'Content-Type': 'application/json'}

def print_response(response, title):
    print(f"\n--- {title} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:", json.dumps(response.json(), indent=2))
    except:
        print("Response (Text):", response.text)

def main():
    # 1. List all contacts
    print("1. Listing all contacts...")
    response = requests.get(f"{BASE_URL}/api/contacts")
    print_response(response, "GET /api/contacts")

    # 2. Create a new contact
    print("\n2. Creating a new contact...")
    new_contact = {
        "name": "API Demo User",
        "email": "api.demo@example.com",
        "phone": "+1234567890"
    }
    response = requests.post(
        f"{BASE_URL}/api/contact/create", 
        data=json.dumps(new_contact), 
        headers=HEADERS
    )
    print_response(response, "POST /api/contact/create")
    
    # Get the ID of the created contact
    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'success':
            contact_id = data.get('id')
            print(f"Created Contact ID: {contact_id}")

            # 3. Get details of the created contact
            print(f"\n3. Getting details for contact {contact_id}...")
            response = requests.get(f"{BASE_URL}/api/contact/{contact_id}")
            print_response(response, f"GET /api/contact/{contact_id}")

            # 4. Update the contact
            print(f"\n4. Updating contact {contact_id}...")
            update_data = {
                "name": "API Demo User (Updated)",
                "phone": "+9876543210"
            }
            response = requests.put(
                f"{BASE_URL}/api/contact/update/{contact_id}", 
                data=json.dumps(update_data), 
                headers=HEADERS
            )
            print_response(response, f"PUT /api/contact/update/{contact_id}")

            # 5. Delete the contact
            print(f"\n5. Deleting contact {contact_id}...")
            response = requests.delete(f"{BASE_URL}/api/contact/delete/{contact_id}")
            print_response(response, f"DELETE /api/contact/delete/{contact_id}")
        else:
            print("Failed to create contact, skipping subsequent steps.")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Odoo. Make sure the server is running on localhost:8069.")
