# 1 балл
# 1. (a + b * c)2                                     2. a - 4 * b / c                                   3. (a * b + 4) / (c - 1)
# 2 балла
# 4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
# 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.
# 6. Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в ней за исключением пробелов встречаются только один раз. Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами, а само слово 'изограмма' - нет.
#
# 4 балла
# 7. Найти сумму десяти первых чисел ряда Фибоначчи.
# 8. В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
# 9. Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу [-1;1], причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]
#
# 8 баллов
# 10. Для заданной матрицы (3*3) найти все ее седловые точки и вернуть список их координат (список списков). Седловых точек может не быть, может быть 1 и более. Например, для матрицы ниже результат должен быть [[1, 0]]:
# 3  8  7
# 5  9  6     <--- седловая точка (1,0)
# 2  6  7
# 11. В двумерном массиве отсортировать четные столбцы по возрастанию, а нечетные - по убыванию
#
# 15 баллов
# 12. Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил начинать каждый урок с того, чтобы задавать каждому ученику пример из таблицы умножения, но в классе 15 человек, а примеры среди них не должны повторяться. В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты). При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)
#
print("Task 1.(1,2,3) ")


def solve_equations(a, b, c):
    if c != 1 and c != 0:
        res_first = (a + b * c) ** 2
        res_second = a - 4 * b / c
        res_third = (a * b + 4) / (c - 1)
        return res_first, res_second, res_third
    elif c == 1:
        res_first = (a + b * c) ** 2
        res_second = a - 4 * b / c
        return res_first, res_second, None
    else:
        res_first = (a + b * c) ** 2
        res_third = (a * b + 4) / (c - 1)
        return res_first, None, res_third


a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

s1, s2, s3 = solve_equations(a, b, c)
print("Answer for the first equation (a + b * c)^2  is %s\n"
      "Answer for the second equation a - 4 * b / c is %s\n"
      "Answer for the third equation (a * b + 4) / (c - 1) is %s\n" % (s1, s2, s3))

print("Task 4.")


def ood_multiply(number):
    multiply_of_odds = 1
    for i in range(len(number)):
        if int(number[i]) % 2 != 0:
            multiply_of_odds *= int(number[i])

    return multiply_of_odds


number = input("Enter your number :")
print("Sum of odd numbers in your number is %d" % ood_multiply(number))

print("Task 5.")


def find_min_dist_to_10(number1, number2):
    if abs(10 - number1) < abs(10 - number2):
        return number1
    elif abs(10 - number1) > abs(10 - number2):
        return number2
    else:
        return None


#
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("Number %d is closer to 10" % find_min_dist_to_10(number1, number2))

print("Task 6.")


def is_isogram(str):
    count = 0
    letters = ""
    for i in str:
        if count > 0:
            return False
        if i in letters and i != ' ':
            count += 1
        letters += i
    return count == 0


string = input("Enter your text")
print("The fact that your string: %s is isogram is %s " % (string, is_isogram(string)))

# 7. Найти сумму десяти первых чисел ряда Фибоначчи.

print("Task 7.")


def sum_fibb_nummers(n):
    result = 0
    for i in range(n + 1):
        result += fib(i)
    return result


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(sum_fibb_nummers(10))

print("Task 8.")

some_list = [0, 1, 2, 3,90,100,-1]


def change_min_max(lst):
    lst = list(lst)
    min_elem = min(lst)
    max_elem = max(lst)
    min_elem_index = lst.index(min_elem)
    max_elem_index = lst.index(max_elem)
    for i in range(len(lst)):
        lst[min_elem_index] = max_elem
        lst[max_elem_index] = min_elem
    return lst


print(change_min_max(some_list))


print("Task 9.")


