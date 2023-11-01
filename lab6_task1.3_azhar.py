#Напишите функцию, которая принимает дату в качестве аргумента и возвращает ее в формате «день.месяц.год»
try:
        def get_date_in_format(date):
            # разделим входную дату по точкам
            date_parts = date.split('.')

            # получаем части даты: год, месяц и день
            year = date_parts[0]
            month = date_parts[1]
            day = date_parts[2]

            # форматируем дату в требуемый вид
            formatted_date = f"{day}.{month}.{year}"

            return formatted_date

    #пример
    input_date = "2023.10.23"
    result = get_date_in_format(input_date)
    print(result)
except SyntaxError:
    print("Oшибки в синтаксисе Python")