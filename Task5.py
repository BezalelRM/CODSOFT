CF = "contacts.txt"

def load():
    contacts = []
    try:
        file = open(CF, "r")
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 4:
                contacts.append({
                    "name": parts[0],
                    "phone": parts[1],
                    "email": parts[2],
                    "address": parts[3]
                })
        file.close()
    except FileNotFoundError:
        pass 
    return contacts

def save(contacts):
    file = open(CF, "w")
    for contact in contacts:
        file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}|{contact['address']}\n")
    file.close()

def add():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = load()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save(contacts)
    print("Contact added successfully.\n")

def view():
    contacts = load()
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search():
    query = input("Enter name or phone number to search: ").lower()
    contacts = load()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("No contact found.\n")

def update():
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep existing value.")
            new_phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New Email ({contact['email']}): ") or contact['email']
            new_address = input(f"New Address ({contact['address']}): ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            save(contacts)
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

def delete():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load()
    new_contacts = []
    found = False
    for contact in contacts:
        if contact['name'].lower() != name:
            new_contacts.append(contact)
        else:
            found = True
    if found:
        save(new_contacts)
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("Contact Book ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            search()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
