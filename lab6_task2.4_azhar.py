#Напишите функцию, которая принимает дату в качестве аргумента и
#возвращает ее разницу с текущей датой. (Возвращает разницу между двумя датами в днях.)
try:
    from datetime import datetime


    def get_difference_between_dates(date1, date2):
        # преобразуем строки даты в объекты datetime
        date1 = datetime.strptime(date1, "%Y.%m.%d")
        date2 = datetime.strptime(date2, "%Y.%m.%d")

        # рассчитаем разницу между двумя датами
        time_difference = date2 - date1

        # извлечем количество дней из разницы во времени
        days_difference = time_difference.days

        return days_difference


    # пример
    date1 = "2023.10.23"
    date2 = "2023.10.24"
    differ = get_difference_between_dates(date1, date2)
    print(differ)
except KeyError:
    print("ошибка в значении ключа")