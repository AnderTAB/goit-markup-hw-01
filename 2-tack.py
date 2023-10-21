def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return f'Invalid command. Додайте add [name] [phone]'

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return f'Invalid command. Додайте change [name] [phone]'
    
    name, new_phone = args
    if name not in contacts:
        return "Контакт не знайдено."

    contacts[name] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Додайте: phone [name]"
    
    name = args[0]
    if name not in contacts:
        return "Контакт не знайдено."
    
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "Контакти не знайдено."
    lst = [f"{name}: {phone}" for name, phone in contacts.items()]
    contact_list = "\n".join(lst)
    return contact_list

def delete_contact(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: delete [name]"
    
    name = args[0]
    if name not in contacts:
        return "Контакт не знайдено."
    
    del contacts[name]
    return "Контакт видалено."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            result = show_phone(args, contacts)
            if result:
                print(result)
            else:
                print("Contact not found.")           
        elif command == "all":
            print(show_all(contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()