from datetime import datetime

birth_date_str = input("please give your birthday in dd.mm.yyyy: ")
birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")

current_date = datetime.now()

age = current_date.year - birth_date.year #计算年龄
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"you are {age} years old now")