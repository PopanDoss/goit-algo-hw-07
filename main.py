from pathlib import Path 
import handler 


# Створюємо функцію для взаємодії користувача з інтерфейсом 
def main():

    print("Welcome to the assistant bot!")
    #Свторюємо цик, що зчитує команди  користувача
    while True:
        user_input = input("Enter a command: ")
        command, *args = handler.parse_input(user_input)
        # Залежно від вказаної команди визначаємо дію користувача
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handler.add_contact(args))
        elif command == "change":
            print(handler.change_contact(args))
        elif command == "phone" :
            print (handler.show_phone(args))
        elif command == "all" :
            print (handler.show_all(handler.book))
        elif command == "add-birthday" :
            print(handler.add_birthday(args))
        elif command == "show-birthday":
            print(handler.show_birthday(args))
        elif command == "birthdays":
            print (handler.birthdays())
        else:
            print("Invalid command.")
            
#Запускаємо функці
if __name__ == "__main__":
    main()