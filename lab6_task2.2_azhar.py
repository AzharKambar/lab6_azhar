#Напишите функцию, которая принимает число «n» в качестве аргумента и возвращает список простых чисел от 2 до n
try:
    def is_prime(num):
        # функция проверки того, является ли число простым
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            # если число делится на любое другое число, оно не является простым
            if num % i == 0:
                return False
        return True


    def get_prime_numbers(n):
        # функция для создания списка простых чисел от 2 до n
        prime_list = []  # Инициализируем пустой список для хранения простых чисел

        for num in range(2, n + 1):
            if is_prime(num):
                prime_list.append(num)

        return prime_list


    # пример:
    n = 100
    result = get_prime_numbers(n)
    print(result)
except SyntaxError:
    print("ошибка в значении ключа")