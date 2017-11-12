
# Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"
# Написать программу, которая преобразует имя студента, ставя фамилию на первое место, а имя на второе. Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.
# Написать программу, которая преобразует имя переменной в формате snake_style в формат CamelizedStyle.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов. Например: ‘employee_first_name’ -> ‘EmployeeFirstName’
# Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. В этой строке указаны имя писателя и через символ * даты рождения и смерти.
# Даты указаны в формате "YYYY-MM-DD". Требуется написать программу, которая по переданной строке определит возраст писателя и вернет его имя и возраст.
# Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна вернуть: 'Leo Tolstoy, 82'.
# Для строки 'Marcus Aurelius*121-04-26*180-03-17' вернуть 'Marcus Aurelius, 59'. Т.е. индексы символов разделителей ('*', '-') незафиксированы!
# Месяцы и дни можно игнорировать.
# 
print("Task 7.")
american_format = input("Enter date in american format: (example:05.17.2016)")
month = str(american_format[0:2])
day = str(american_format[3:5])
year = str(american_format[6:])
print("Date in european format: %s.%s.%s" % (day, month, year))

print("\nTask 8.")

students_name = input("Enter student’s name: (example: Mark Zuckerberg)")
name_split = students_name.split(" ")
name = name_split[0]
surname = name_split[1]
print("Transformation complete:")
print("%s  -> %s %s" % (students_name, surname, name))

print("\nTask 9.")
snake_style = input("Enter the name of variable in the snake_style: (example: snake_style_variable)")
split = (snake_style.split('_'))
first_part = str(split[0])
second_part = str(split[1]).capitalize()
third_part = str(split[2]).capitalize()
camel_style = first_part+second_part+third_part
print("Transformation complete:")
print("%s -> %s" % (snake_style, camel_style))

print("\nTask 10.")
print("Some information about person: 'Leo Tolstoy*1828-08-28*1910-11-20'")
info = "Leo Tolstoy*1828-08-28*1910-11-20"
info_split = info.split('*')
persons_name = info_split[0]
birth_date = info_split[1]
death_date = info_split[2]
birth_split = birth_date.split("-")
death_split = death_date.split("-")
birth_year = int(birth_split[0])
death_year = int(death_split[0])
age = death_year - birth_year
print("Person’s name and age:")
print("%s , %d" % (persons_name, age))

print("\nSome information about person: 'Marcus Aurelius*121-04-26*180-03-17")
info = 'Marcus Aurelius*121-04-26*180-03-17'
info_split = info.split('*')
persons_name = info_split[0]
birth_date = info_split[1]
death_date = info_split[2]
birth_split = birth_date.split("-")
death_split = death_date.split("-")
birth_year = int(birth_split[0])
death_year = int(death_split[0])
age = death_year - birth_year
print("Person’s name and age:")
print("%s , %d" % (persons_name, age))




