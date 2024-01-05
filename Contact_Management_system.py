import json

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist yet

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def add_contact(self, name, phone_number, email):
        contact = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")

    def edit_contact(self, index, name, phone_number, email):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = {'name': name, 'phone_number': phone_number, 'email': email}
            self.save_contacts()
            print(f"Contact at index {index} edited successfully.")
        else:
            print("Invalid index. No contact edited.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f"Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid index. No contact deleted.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact_manager.add_contact(name, phone_number, email)
            
        elif choice == '2':
            contact_manager.view_contacts()
            
        elif choice == '3':
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter the new name: ")
            phone_number = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            contact_manager.edit_contact(index, name, phone_number, email)
            
        elif choice == '4':
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)
            
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()