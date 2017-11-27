import random
# Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
# def get_max_digit(number): # returns int
# 		     pass
#
# Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы в зависимости от первых букв их фамилии.
#  Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’. Название группы определяет в какую группу попадает абитуриент, в зависимости от первой буквы его/ее фамилии.
# Например, Will Smith попадает в группу ‘Q-T’, т.к. первая буква его фамилии попадает в диапазон букв от Q до Т (включительно!). Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д.
# Написать функцию, которая получает список имен студентов вида ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах, сформированных по их фамилиям, описанным выше образом.
#      def group_by_surname(list_of_enrollees): # returns 4 ints
# 			pass
#
# Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать. Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше. После чего опять просит угадать. И так пока пользователь не угадает выбранное число.
#
# Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную, на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске, если на первую клетку положить одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д. Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен). Посчитайте, начиная с какой клетки по счету, общее количество зерен, которое должен был бы отдать раджа изобретателю было больше 1 000 000 зерен и сколько конкретно зерен он должен был бы отдать.
#      def chess_reward(): # returns 2 ints
# 			pass

print("Task 21")


def get_max_digit(number):
    digits = ''
    for symbol in str(number):
        if symbol.isdigit():
            digits = digits + symbol
    number = max(digits)
    return int(number)


print("Max digit form number is %d" % get_max_digit(1234567891012))


print("\nTask 22")

list_of_enrollees = ['Name1 Aurname1', 'Name2 Jurname2', 'Name3 Zurname3']


def group_by_surname(list_of_enrollees): # returns 4 ints
    ai_group = 0
    jp_group = 0
    qt_group = 0
    uz_group = 0

    for enrollees in list_of_enrollees:
        surname_first_letter = enrollees.split(" ")
        if ord(surname_first_letter[1][0]) in range(ord('A'), ord('I')+1):
            ai_group += 1
        elif ord(surname_first_letter[1][0]) in range(ord('J'), ord('P')+1):
            jp_group += 1
        elif ord(surname_first_letter[1][0]) in range(ord('Q'), ord('T')+1):
            qt_group += 1
        elif ord(surname_first_letter[1][0]) in range(ord('U'), ord('Z')+1):
            uz_group += 1
        else:
            print("Wrong surname in list!")

    return ai_group, jp_group, qt_group, uz_group


ai_group, jp_group, qt_group, uz_group = group_by_surname(list_of_enrollees)
print("Amount of enrollees in groups:\n A - I group: %d\n J - P group: %d\n Q - T group: %d\n U - Z group: %d" % (ai_group,jp_group,qt_group,uz_group))


print("\nTask 23")

number = random.randint(1, 10)

print("Try to guess the number from 1 to 10!")

while True:
    user_number = int(input("Enter your number here :"))
    if 1 > user_number or user_number > 10:
        print("Wrong number! [1-10]")
    else:
        if user_number != number:

            if user_number > number:
                print("Secret number is less! Try again.")
            else:
                print("Secret number is greater! Try again.")
        else:
            print("You win! It is %d" % number)
            break

print("\nTask 24")


def chess_reward():
    result = 1
    cage = 0
    flag = True
    for i in range(64):
        result = result*2
        if flag:
            if result > 10000000:
                cage = i
                flag = False
    result = result - 1
    return cage, result


cage, result = chess_reward()
print("Number of grains is %d and million of grains was achieved on the %d cage." % (result, cage))