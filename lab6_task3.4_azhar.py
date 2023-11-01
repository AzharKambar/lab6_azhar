#Напишите функцию, которая принимает список слов в качестве аргумента
#и возвращает список слов, начинающихся с гласной
try:
    def get_words_starting_with_vowel(words):
        # задаем список гласных
        vowels = ['a', 'e', 'i', 'o', 'u']

        # используем понимание списка, чтобы фильтровать слова, начинающиеся с гласной
        vowel_words = [word for word in words if word[0].lower() in vowels]

        return vowel_words


    # пример
    input_words = ["apple", "banana", "orange", "bear", "cat"]

    vowel_result = get_words_starting_with_vowel(input_words)
    print(vowel_result)
except KeyError:
    print("ошибка в значении ключа")