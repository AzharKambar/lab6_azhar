#Напишите функцию, которая принимает в качестве аргумента
# список чисел и возвращает список, содержащий все элементы, встречающиеся в списке не более двух раз.
try:
    def get_elements_with_no_more_than_two_occurrences(lst):
        # создаем пустой список для хранения элементов, встречающихся не более двух раз
        empt = []

        # создаем словарь для подсчета количества вхождений каждого элемента
        element_counts = {}

        # проходим по списку и увеличиваем счетчик для каждого элемента
        for item in lst:
            if item in element_counts:
                element_counts[item] += 1
            else:
                element_counts[item] = 1

        # проходим по словарю с подсчетами и добавляем элементы, встречающиеся не более двух раз, в результат
        for key, value in element_counts.items():
            if value <= 2:
                empt.append(key)

        return empt


    # пример:
    my_list = [1, 2, 3, 1, 2, 4]
    empt = get_elements_with_no_more_than_two_occurrences(my_list)
    print(empt)
except KeyError:
    print("ошибка в значении ключа")