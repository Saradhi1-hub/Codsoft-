import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully.\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    contacts = load_contacts()
    found = [c for c in contacts if c['name'].lower() == name.lower()]
    if found:
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print("❌ Contact not found.")
    print()

def delete_contact():
    name = input("Enter name to delete: ")
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(updated) != len(contacts):
        save_contacts(updated)
        print("🗑️ Contact deleted.\n")
    else:
        print("❌ Contact not found.\n")

def main():
    while True:
        print("📒 Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        print()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("📕 Exiting Contact Book. Bye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
      
