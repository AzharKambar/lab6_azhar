#Напишите функцию, которая принимает список в качестве аргумента и возвращает словарь,
# содержащий уникальные элементы списка и их количество.
try:
    def get_unique_elements_with_count(input_list):
        # инициализируйте пустой словарь для хранения счетчиков
        unique_counts = {}

        # перебирает элементы в списке
        for item in input_list:
            # если элемент уже есть в словаре, увеличиваем его счетчик
            if item in unique_counts:
                unique_counts[item] += 1
            # если элемента нет в словаре, добавьте его со счетчиком 1
            else:
                unique_counts[item] = 1

        return unique_counts


    # пример:
    input_list = [1, 2, 3, 1, 2, 4, 1, 2]
    result = get_unique_elements_with_count(input_list)
    print(result)
except KeyError:
    print("ошибка в значении ключа")