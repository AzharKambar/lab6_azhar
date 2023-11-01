try:
    def keys_true(input_dict):
        #создаем пустой список для хранения ключей со значением True
        keys_true= []

        #перебираем пары ключ-значение в словарь
        for key, value in input_dict.items():
            #проверяем соответствует ли значение True.если значение истинно:
                # Если да, добавляем ключ в список keys_true
                keys_true.append(key)

        #возвращаем список ключей со значением True
        return keys_true

    #пример словаря:
    my_dict = {
        "a": True,
        "b": False,
        "c": True
    }

    result = keys_true(my_dict)
    print(result)

except SyntaxError:
    print("Oшибки в синтаксисе Python")