import math
# Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли, без использования операторов цикла.
# А теперь без строк :)
# Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.

print("*****************Task 11*****************")


def print_for_cos(degrees, value):
    print('-------------------------------------')
    print('Cosine of %d degrees = %f' % (degrees, value))


def degrees_in_radians(degrees):
    return degrees * (math.pi / 180)

own_value = int(input("Enter degrees(except 60, 45, 40): "))
print_for_cos(60, math.cos(degrees_in_radians(60)))
print_for_cos(45, math.cos(degrees_in_radians(45)))
print_for_cos(40, math.cos(degrees_in_radians(40)))
print_for_cos(own_value, math.cos(degrees_in_radians(own_value)))


print("\n*****************Task 12*****************")


def sum_of_digits(value):
    a = value // 100
    b = value % 100 // 10
    c = value % 10
    print("Let’s count: %d + %d + %d" % (a, b, c))
    return a + b + c


number = int(input("Enter a three-digit number: "))
print("Sum of digits in your number is: %d" % sum_of_digits(number))

print("\n*****************Task 13*****************")


def triangle_square_and_perimeter (cathetus_a, cathet_b):
    square = (cathetus_a * cathet_b) / 2
    hypotenuse = math.sqrt(cathetus_a ** 2 + cathet_b ** 2)  # Мы не можем найти периметр без гипотенузы, поэтому ее необходимо посчитать
    perimeter = cathetus_a + cathet_b + hypotenuse
    return square, perimeter, hypotenuse


def print_for_triangle(square, perimeter,hypotenuse):
    print('-------------------------------------')
    print('Result:')
    print('-------------------------------------')
    print('Square of a triangle = %d sq.cm.\n'
          'Perimeter of a triangle = %d cm.\n'
          'Where:\n'
          '\t cathetus A = %d cm.\n'
          '\t cathetus B = %d cm.\n'
          '\t hypotenuse = %d cm.' % (square, perimeter,cathetus_a,cathetus_b, hypotenuse))
    print('-------------------------------------')


cathetus_a = int(input("Enter the length of cathetus A:"))
cathetus_b = int(input("Enter the length of cathetus B:"))

square, perimeter, hypotenuse = triangle_square_and_perimeter(cathetus_a,cathetus_b)
print_for_triangle(square, perimeter, hypotenuse)