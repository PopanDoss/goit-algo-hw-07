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
        massage = "Contact added."
        return massage
    else :
        massage = "Contact already exists"
        return massage

#Функція, що змінює номер 
@input_error
def  change_contact(args):
    name, phone = args
    record = book.find(name)

    if record:
        oldphone = record.phones[0].value
        record.edit_phone(oldphone, phone)
        massage =  f"Phone {oldphone} changed to {phone}" 
        return massage
    else:
        massege = f"Contact {name} not found"
        return massage

#Функція, що відображає телефон  
@input_error
def show_phone(args) :
    name = args[0] 
    record = book.find(name)

    if record :    
        result = ', '.join(map(str, record.phones))
        massage = f"Contact {name} phone {result}"
        return massage
    else:
        massage = f"Contact {name} not found"
        return massage

#Функція,що відображає всі записи
@input_error
def show_all(book):

    if len(book)>0 :
        message = book.__str__()
        return message
    else: 
        message = "Сontact list is empty"
        return message
    
#Функція, що додає дні народження 
@input_error
def add_birthday(args):
    name = args[0]
    bdays = args[1]
    record = book.find(name)

    if record :
        record.add_birthday(bdays)
        message = "Birthday added"
        return message
    else:
        message = f"Contact {name} not found"
        return message

#Функція, що показує день народження
@input_error
def show_birthday(args):
    name = args[0] 
    record = book.find(name)

    if record:
        if record.birthday:
            bday = record.birthday.value 
            message =  f"Contact name: {name}, birthday: {bday}"    
            return message
        else :
            message = f" Contact {name} birthday not found"
            return message
    else:
        message = f"Contact {name} not found"
        return message

#Функція, що виводить всі дні народження 
@input_error
def birthdays():
    message = book.get_upcoming_birthdays()
    return message


     

