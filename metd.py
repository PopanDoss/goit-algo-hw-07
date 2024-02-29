from collections import UserDict
from datetime import datetime as dtdt
import datetime as dt
import re 

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
            super().__init__(value)
        else :
            raise ValueError ("Incorrect Name")

class Phone(Field):
    def __init__(self, value):
        if  str.isdigit(value) and len(value) == 10:
            super().__init__(value)
        else :
            raise ValueError ("Incorrect phone format")
        
class Birthday(Field):
    def __init__(self, value):
        pattern= r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])\.(0[1-9]|1[0-2])\.([0-9][0-9][0-9][0-9])"
           
        if re.match(pattern, value) :
            super().__init__(value)
        else:
            raise ValueError ("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone (self, phone ) :
          self.phones.append(Phone(phone)) 
    
    def remove_phone(self, phone):
        for  ph in self.phones:
            if ph.value == phone:
               self.phones.remove(ph)
           
    def edit_phone(self, oldphone, newphone):
        newphone = Phone(newphone)
        for ph in self.phones:
            if ph.value ==oldphone :
                ph.value = newphone.value
                break
        else :
            raise ValueError ("Phone not found")
             
    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone :
                return ph
            
    def add_birthday (self, birthday) :
         self.birthday = (Birthday(birthday))
         return self.birthday  
            
    def getRecord (self):
        return self.name.value, self.phones

    def __str__(self):
        if self.birthday :
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"
        else: 
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def delete(self, namephone):
        for name in self.data:
            if name == namephone :
                return self.data.pop(name)
            
    def find(self, namephone):
        if namephone in self.data :
            return self.data[namephone]
        

    def get_upcoming_birthdays (self):
        
        list_birthday_days = []
        today = dtdt.today().date()
       
        for user in self.data.values():
            
            if user.birthday : 
                
                birthday = user.birthday.value[:6]+str(today.year)
                birthday_this_year = dtdt.strptime(birthday, "%d.%m.%Y").date()        
                
                if birthday_this_year < today:
                    pass
            
                else:
                    different_day = (birthday_this_year - today).days
                    if 7>= different_day>=0:

                        #Якщо так, визначаємо який це день тижня
                        day_in_week = birthday_this_year.isoweekday()

                        #Змінюємо дату на понеділок,якщо вона потрапляєна на вихідні, та додаємо словником у список
                        if day_in_week <6 :
                            list_birthday_days.append({"name":user.name.value, "birthday": birthday})
                        elif day_in_week == 6:
                            list_birthday_days.append({"name":user.name.value, "birthday": (birthday_this_year + dt.timedelta(days=2)).strftime("%d.%m.%Y")})
                        else :
                            list_birthday_days.append({"name":user.name.value, "birthday": (birthday_this_year + dt.timedelta(days=1)).strftime("%d.%m.%Y")})

        #Повертаємо отриманий список словників
        return list_birthday_days 

    def __str__(self) :
        result = []
        
        for record in self.data.values():
            
            if record.birthday:
                contact = f'Contact name: {record.name.value}, phones : {str([p.value for p in record.phones]) }, birthday: {record.birthday.value}'
                result.append(contact)

            else:
                contact = f'Contact name: {record.name.value}, phones : {str([p.value for p in record.phones])}'
                result.append(contact)

        return "\n".join(result)
    

  

if __name__ == "__main__":
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("25.02.2024")

    john_record.find_phone("John")

    sofi_records = Record("Sofi")
    sofi_records.add_phone("0950857323")
  
    book = AddressBook()
    book.add_record(john_record)

    for name, record in book.data.items():
        print(record)

    bday = book.get_upcoming_birthdays()
    print(bday)

    print(book.find("John"))
    

  

