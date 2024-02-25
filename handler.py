import metd
from functools import wraps

book = metd.AddressBook()

#Створюємо декоратор для обробки помилок 
def input_error(func) :
    def inner(*args, **kwargs) :
        try :
            return func(*args, **kwargs)
        except ValueError:
            print(ValueError)
            return "Enter the argument for the command"
        except KeyError :
            print(KeyError)
            return  "Name is Not Found"
        except IndexError :
            print(IndexError)
            return "Enter the argument for the command"
    return inner


#функція, що зчитує команду та значення
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#функція, що додає новий запис в список 
@input_error
def add_contact(args):

    name, phone = args
    if name not in book :
        name = metd.Record(name)
        name.add_phone(phone)
        book.add_record(name)
        return "Contact added."
    else :
        return "Contact already exists"

#Функція, що змінює номер 
@input_error
def  change_contact(args):
    name, phone = args
    if name in book :
        print (book.find(name))
        oldphone = input("What number needs to be changed?  " )
        book[name].edit_phone(oldphone, phone)
        return f"Phone {oldphone} changed to {phone}" 
    else:
            return f"Contact {name} not found"

#Функція, що відображає телефон  
@input_error
def show_phone(args) :
    name = args[0] 
    if name in book:    
        phones = ','.join(p.value for p in book.find(name).phones)
        return f"Contact name: {name}, phones: {phones}"
    else:
        return f"Contact {name} not found"

#Функція,що відображає всі записи
@input_error
def show_all(book):
    if len(book)>0 :
        for name, record in book.data.items():
            print(record)
    else: 
        return "Сontact list is empty"
    
#Функція, що додає дні народження 
@input_error
def add_birthday(args):
    name = args[0]
    bdays = args[1]
    if name in book :
        book[name].add_birthday(bdays)
        return "Birthday added"
    else:
        return f"Contact {name} not found"

@input_error
def show_birthday(args):
    name = args[0] 
    result = book.find(name)
    if result.birthday:     
        return f"Contact name: {name}, birthday: {result.birthday.value}"
    else:
        return f"Contact {name} not found"

#Функція, що виводить всі дні народження 
@input_error
def birthdays():
    return book.get_upcoming_birthdays()


     

