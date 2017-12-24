#Написать функцию, возвращающую все простые числа от 1 до 100.


def gen_primes():
    lst = []
    for i in range(1, 101):
        if i == 1:
            pass
        else:
            for j in lst:
                if i % j == 0:
                    break
            else:
                lst.append(i)
    return lst


print(gen_primes())