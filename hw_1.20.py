import math
import random

# Написать функцию решения квадратного уравнения.
# 		def solve_quadratic_equation(a, b, c): # return 2 values
# 			pass
#
# Каждому символу в таблице символов Unicode соответствует число. Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
# 		def sum_symbol_codes(first, last): # returns int
# 			pass
#
# Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
# 		def find_min_max_diff(num_limit, lower_bound, upper_bound): # returns int
# 			pass
#
# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди 100 случайно сгенерированных чисел в произвольном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
# 		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
# 		     pass


print("Task 1.17")


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        return x1, None
    else:
        return None, None


a = int(input("Enter the value for a"))
b = int(input("Enter the value for b"))
c = int(input("Enter the value for c"))

x1, x2 = solve_quadratic_equation(a, b, c)
if x1 is None:
    print("No roots")
else:
    print("The square roots of your equation are: \nx1 = %.2f\nx2 = %.2f" % (x1, x2))

print("Task 1.18")


def sum_symbol_codes(first, last):
    first_symbol = ord(first)
    last_symbol = ord(last)
    result = 0
    for symbol_code in range(first_symbol, last_symbol+1):
        result += symbol_code
    return result


first = input("Enter the first symbol")
last = input("Enter the last symbol")
print("Sum of symbol codes is %d" % sum_symbol_codes(first, last))


print("Task 1.19")


def find_min_max_diff(num_limit, lower_bound, upper_bound):
    min_num = upper_bound
    max_num = lower_bound
    for number in range(num_limit):
        digit = random.randint(lower_bound, upper_bound)
        if digit <= min_num:
            min_num = digit
        if digit >= max_num:
            max_num = digit
    return max_num - min_num


num_limit = int(input("Enter the limit of numbers: "))
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
print("Difference between min number and max number is %d" % find_min_max_diff(num_limit, lower_bound, upper_bound))

print("Task 1.20")


def diff_even_odd(lower_bound, upper_bound):
    even_sum = 0
    odd_sum = 0
    for number in range(100):
        digit = random.randint(lower_bound, upper_bound)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return even_sum - odd_sum


lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
print("Difference between even and odd numbers is %d" % diff_even_odd(lower_bound, upper_bound))
