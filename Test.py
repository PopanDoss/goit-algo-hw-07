 
from collections import UserDict
from datetime import datetime as dtdt
import re 
import datetime as dt


users = [
    {"name": "John Doe", "birthday": "1991.02.03"},
    {"name": "Jane Smith", "birthday": "1990.02.01"}]

def get_upcoming_birthdays (self):
        
        list_birthday_days = []
        today = dtdt.today().date()
       
        for user in users:
            
            birthday = user['birthday']
            birthday = birthday[:4]+str(today.year)
            birthday_this_year = dtdt.strptime(birthday, "%Y.%m.%d").date()        
            
            if birthday_this_year < today:
                pass
           
            else:
                different_day = (birthday_this_year - today).days
                if 7>= different_day>=0:

                    #Якщо так, визначаємо який це день тижня
                    day_in_week = birthday_this_year.isoweekday()

                    #Змінюємо дату на понеділок,якщо вона потрапляєна на вихідні, та додаємо словником у список
                    if day_in_week <6 :
                        list_birthday_days.append({"name":user["name"], "birthday": birthday})
                    elif day_in_week == 6:
                        list_birthday_days.append({"name":user["name"], "birthday": (birthday_this_year + dt.timedelta(days=2)).strftime("%d.%m.%Y")})
                    else :
                        list_birthday_days.append({"name":user["name"], "birthday": (birthday_this_year + dt.timedelta(days=1)).strftime("%d.%m.%Y")})

        #Повертаємо отриманий список словників
        return list_birthday_days 


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні: ", upcoming_birthdays)