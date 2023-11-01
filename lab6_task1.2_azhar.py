try:
        def get_unique_elements(lst):
            #создаем пустой список для хранения уникальных элементов
            unique_elem = []

            #создаем словарь для подсчета количества вхождений каждого элемента
            elem_counts = {}

            #проходим по списку и увеличиваем счетчик для каждого элемента
            for item in lst:
                if item in elem_counts:
                    elem_counts[item] += 1
                else:
                    elem_counts[item] = 1

            #проходим по словарю с подсчетами и добавляем уникальные элементы в список
            for key, value in elem_counts.items():
                if value == 1:
                    unique_elem.append(key)

            return unique_elem

    #пример:
    my_list = [1, 2, 3, 1, 2, 4]
    result = get_unique_elements(my_list)
    print(result)
except SyntaxError:
    print("Oшибки в синтаксисе Python")