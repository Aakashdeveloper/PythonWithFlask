# Initialize the contact list
contacts = []  # Create an empty list to store contacts

# Function to add a contact
def add_contact(contact_list, name, phone):
    # Create a dictionary with the contact's name and phone number
    contact = {"name": name, "phone": phone}
    # Add the contact to the contact list
    contact_list.append(contact)
    # Print a success message
    print(f"Contact {name} added successfully.")
    # Display the updated contact list
    view_contacts(contact_list)

# Function to view all contacts
def view_contacts(contact_list):
    # Check if the contact list is empty
    if not contact_list:
        # Print a message if no contacts are found
        print("No contacts found.")
    else:
        # Loop through each contact in the contact list
        print("Current contacts:")
        for contact in contact_list:
            # Print the contact's name and phone number
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

# Function to search for a contact by name
def search_contact(contact_list, name):
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}")
            view_contacts(contact_list)
            return
    print("Contact not found.")
    view_contacts(contact_list)

# Function to delete a contact by name
def delete_contact(contact_list, name):
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            contact_list.remove(contact)
            print(f"Contact {name} deleted successfully.")
            view_contacts(contact_list)
            return
    print("Contact not found.")
    view_contacts(contact_list)

# Main program
print("Welcome to the Contact Management System.")

while True:
    print("\nPlease choose an option:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(contacts, name, phone)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        name = input("Enter the name of the contact to search for: ")
        search_contact(contacts, name)
    elif choice == "4":
        name = input("Enter the name of the contact to delete: ")
        delete_contact(contacts, name)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
