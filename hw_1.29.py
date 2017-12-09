import random
import string
# Создайте список на 50 элементов из всех нечётных чисел от 1 до 99 и передайте его в функцию, которая перемешает его элементы в случайном порядке
# (например, 99 11 43 19 … 7 91 3 1).
# Примечание: использовать метод random.shuffle не допускается.

# Создайте список из 11 случайных целых чисел из отрезка [-1;1].
# Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
#  Если два каких-то элемента встречаются одинаковое количество раз, то вернуть None.
#
# Напишите функцию, которая преобразует переданный ей текст подобным описанным выше образом. В качестве алгоритма перемешивания букв в слове используйте следующий:
#
# Для каждого слова в тексте:
# 	1. Фиксируем первый и последний символы слова.
# 	2. Из оставшихся берём первые три символа, произвольно перемешиваем.
# 	3. Полученную тройку фиксируем, т.е. она уже не будет участвовать в дальнейшем перемешивании.
# 	4. Повторяем пункт 2, пока незафиксированные символы не кончатся.
#
# Создать программу, которая запрашивает у пользователя произвольную строку символов. Далее программа ее шифрует и выводит на экран в зашифрованном виде.
# Шифрование происходит путем замены каждого символа символом, который находится на 5 позиций правее в предопределенной таблице шифрования.
# Таблица шифрования задается программистом в виде одномерного списка символов латинского алфавита от a до z.
#  Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
# 	Таблица шифрования (a,b,c,d,...,x,y,z,1,2,3,4,5,6,7,8,9,0)
# 	Например: Исходная строка, которую ввел пользователь: 'secret'
# 	Зашифрованная строка, которую выдала программа: 'xjhwjy'
# 	Примечание: т.н. таблица шифрования может быть представлена как строка или список.
#
# def encode(str_to_encode): # returns enсoded string
# 		pass
# Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# Пароль состоит из 8 символов
# В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# Пароль обязательно должен содержать Большие и маленькие буквы и цифры


print("Task 1.25")
lst = [i for i in range(1, 100, 2)]
print(lst)


# def shuffle_list(list_to_shuffle):  # no return (shuffles list in place)
#     empty_list = []
#     while len(list_to_shuffle) != 0:
#         elem_of_list = random.choice(list_to_shuffle)
#         empty_list.append(elem_of_list)
#         list_to_shuffle.remove(elem_of_list)
#     print(empty_list)

def shuffle_list(list_to_shuffle):  # no return (shuffles list in place)
    for i in list_to_shuffle:
        elem = random.choice(list_to_shuffle)
        list_to_shuffle.remove(elem)
        list_to_shuffle.append(elem)

    print(list_to_shuffle)


shuffle_list(lst)


print("Task 1.26")


def calc_frequency(lst):
    lst = list(lst)
    first_group = []
    second_group = []
    third_group = []
    for elem in range(len(lst)):
        if lst[elem] == -1:
            first_group.append(lst[elem])
        elif lst[elem] == 0:
            second_group.append(lst[elem])
        else:
            third_group.append(lst[elem])
    a = len(first_group)
    b = len(second_group)
    c = len(third_group)
    if (a == b and a != 0) or (b == c and b != 0) or (c == a and c != 0):
        return None
    elif a > b and a > c:
        return first_group[0]
    elif b > a and b > c:
        return second_group[0]
    elif c > a and c > b:
        return third_group[0]


lst1 = [random.randint(-1, 1) for i in range(11)]
print(lst1)

print(calc_frequency(lst1))

print("Task 1.27")


text = 'Some text for this shuffle'


def shuffle_text(text):
    word_list = text.split()
    new_text = ''
    for words in word_list:
        middle = words[1:-1]
        middle = list(middle)
        random.shuffle(middle)
        middle_part = ''.join(middle)
        new_word = ''.join(words[0] + middle_part + words[-1])
        new_text = new_text + new_word + ' '

    return print(new_text)


shuffle_text(text)

print("Task 1.28")

def encode(str): # returns enсoded string

    str = list(str)
    for letter in range(len(str)):
        symbol = ord(str[letter])
        if symbol == 32:
            pass
        else:
            symbol = chr(symbol + 5)
            str.pop(letter)
            str.insert(letter, symbol)
    encoded = "".join(str)


    return encoded


to_code = input("Please. enter the text for encode:")
print("Your encoded text :%s" % encode(to_code))


print("Task 1.29")


def gen_password():  # returns string

    password = ''
    for i in range(5):
        password = password + ''.join(random.choice(string.ascii_lowercase + random.choice(string.ascii_uppercase + random.choice(string.digits ))))
    password = password + ''.join(random.choice(string.ascii_lowercase))
    password = password + ''.join((random.choice(string.ascii_uppercase)))
    password = password + ''.join((random.choice(string.digits)))

    return password


password = gen_password()
print(password)

