#Напишите функцию, которая принимает список покупок в качестве аргумента
#возвращает список покупок, отсортированный по цене.
try:
    def sort_by_price(shopping_list):
        # используем функцию sorted с лямбда-функцией в качестве ключа для сортировки по цене
        sorted_list = sorted(shopping_list, key=lambda item: item["price"])

        return sorted_list


    # пример
    input_shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]

    sort_result = sort_by_price(input_shopping_list)
    print(sort_result)
except KeyError:
    print("ошибка в значении ключа")