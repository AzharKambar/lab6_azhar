#Напишите функцию, которая принимает список чисел в качестве аргумента и
#возвращает список, содержащий все элементы, являющиеся совершенными числами
try:
    def is_perfect_number(num):
        # совершенное число – это целое положительное число, равное сумме своих собственных делителей.Совершенные числа больше 1.
        # правильные делители — это положительные делители числа, исключая само число
        if num <= 1:
            return False

            # Найдем сумму собственных делителей числа.1 всегда является делителем любого положительного целого числа
        divisors_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                # не пересчитываем один и тот же делитель дважды
                if i != num // i:
                    divisors_sum += num // i

        # проверяем, равна ли сумма делителей самому числу
        return divisors_sum == num


    def get_perfect_numbers(numbers):
        perfect_numbers = []
        for num in numbers:
            if is_perfect_number(num):
                perfect_numbers.append(num)
        return perfect_numbers


    # пример:
    numbers = [6, 28, 12, 496, 8, 15]
    perfect_nums = get_perfect_numbers(numbers)
    print(perfect_nums)
except KeyError:
    print("ошибка в значении ключа")