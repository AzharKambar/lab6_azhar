#Напишите функцию, которая принимает список чисел в качестве аргумента и
# возвращает список, содержащий все элементы, которые являются простыми числами.
try:
        def is_prime(num):
        #1 и числа меньше или равные 1 не являются простыми
        if num <= 1:
            return False
            # 2 и 3 — простые числа
        if num <= 3:
            return True
            # Числа, делящиеся на 2 или 3, не являются простыми
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            # проверяем делимость числа до квадратного корня
            if num % i == 0 or num % (i + 2) == 0:
                return False
            # Если ни одно из вышеперечисленных условий не выполнено, число является простым
            i += 6
        return True
    def get_prime_numbers_in_list(numbers):
        prime_numbers = []
        for num in numbers:
        #Если число простое, добавить его в список prime_numbers
        return prime_numbers  # Возвращаем список простых чисел
        if is_prime(num):
            prime_numbers.append(num)


    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
    output_list = get_prime_numbers_in_list(input_list)
    print(output_list)
except KeyError:
    print("ошибка в значении ключа")