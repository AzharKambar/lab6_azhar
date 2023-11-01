#Напишите функцию, которая принимает строку в качестве аргумента и
# возвращает список всех слов в строке, разделенных пробелами
try:
    def get_words_from_string(string):
        #разделяем строку на слова, используя пробелы в качестве разделителя
        words = string.split()
        return words


    #пример:
    input_string = "This a string with a several words."
    result = get_words_from_string(input_string)
    print(result)
except SyntaxError :
    print("Oшибки в синтаксисе Python")