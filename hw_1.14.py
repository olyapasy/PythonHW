# Написать функцию, которая будет проверять четность некоторого числа.
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.
# Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.


print('Task 1.')


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


value = int(input("Enter the value:"))
print(is_even(value))

if bool(is_even(value)) == 1:
    print('Your value %d is even' % value)
else:
    print('Your value %d is not even' % value)


print('\nTask 2.')


def is_intersect(x1, y1, radius1, x2, y2, radius2):
    distance_between_centers = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    if distance_between_centers > radius1 + radius2:
        return False
    else:
        return True


x1 = int(input("Enter coordinate x for the first center:"))
y1 = int(input("Enter coordinate y for the first center:"))
radius1 = int(input("Enter the radius for the first center:"))

x2 = int(input("Enter coordinate x for the second center:"))
y2 = int(input("Enter coordinate y for the second center:"))
radius2 = int(input("Enter the radius for the second center:"))

print(is_intersect(x1, y1, radius1, x2, y2, radius2))

if bool(is_intersect(x1, y1, radius1, x2, y2, radius2)) == 0:
    print("Circles not intersect")
else:
    print("Circles intersect")


print('\nTask 3.')


def is_crash(speed1, speed2):
    time1 = 4 / speed1
    time2 = 6 / speed2
    if time1 > time2:
        return True
    else:
        return False


speed1 = int(input("Enter speed of the first train"))
speed2 = int(input("Enter speed of the second train"))
print(is_crash(speed1, speed2))

if bool(is_crash(speed1, speed2)) == 1:
    print("Bang!The big crash is happened.")
else:
    print("No crash.")

