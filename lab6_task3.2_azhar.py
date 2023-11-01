#Напишите функцию, которая принимает список чисел в качестве аргумента и
#возвращает список, содержащий все элементы, являющиеся правильными квадратами.
try:
    import math


    def is_perfect_square(num):
        # проверяем, является ли квадратный корень числа целым числом
        return math.isqrt(num) ** 2 == num


    def find_perfect_squares(numbers):
        # инициализируем пустой список для хранения идеальных квадратов.
        perfect_squares = []

        # перебираем список ввода
        for num in numbers:
            if is_perfect_square(num):
                perfect_squares.append(num)

        return perfect_squares


    # пример
    input_numbers = [4, 25, 81]
    final_sq = find_perfect_squares(input_numbers)
    print(final_sq)
except KeyError:
    print("ошибка в значении ключа")