from collections import defaultdict 
import calendar
from datetime import datetime

# Змінюємо рік народження всіх контактів на теперішній рік
def birthday_this_year(user):
    today = datetime.today().date()
    name = user["name"]
    birthday = user["birthday"].date() 
    birthday_this_year = birthday.replace(year=today.year)
    return {"name" : name,  "birthday": birthday_this_year}
# Створюємо список іменниників на наступні 7 днів
def full_list_for_the_next_7_day(users):
    full_dict = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 
     'Thursday': [], 'Friday': []}

    current_date = datetime.today().date()
    current_day = current_date.weekday()

    users = map(birthday_this_year, users)
    for user in users:
        difference = user["birthday"] - current_date

# Якщо сьогодні понеділок то не враховуємо людей, в яких день народження у вихідний день
        if current_day == 0 and difference.days <= 5 and difference.days > 1:
            week_day = datetime.strftime(user["birthday"], '%A')
            full_dict[week_day].append(user["name"])
        
        if current_day > 0 and difference.days <= 7 and difference.days > 1:
            week_day = datetime.strftime(user["birthday"], '%A')
            if week_day == 'Saturday' or week_day == 'Sunday':
                week_day = 'Monday'
            full_dict[week_day].append(user["name"])
    
    return full_dict

def get_birthdays_per_week(users):
    spisok = full_list_for_the_next_7_day(users)

    for day, names in spisok.items():
        if names:
            names_str = ", ".join(names)
            print(f'{day}: {names_str}')

users =[
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 19)},
    {"name": "Galia Kvitka", "birthday": datetime(1997, 10, 22)},
    {"name": "Alina Balaba", "birthday": datetime(2003, 10, 24)},
    {"name": "Serhii Stepanenko", "birthday": datetime(1992, 10, 25)},
    {"name": "Alex Melnykov", "birthday": datetime(1988, 10, 26)}
]
result = get_birthdays_per_week(users)
