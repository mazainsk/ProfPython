"""
Морфологический анализ слова на базе библиотеки pymorphy2
"""
# pip install pymorphy2
# pip install num2words
# Версия Python должна быть не выше 3.10

from pymorphy2 import MorphAnalyzer
from modules_packages.n2w import n2w

def mt(text, lex=False):
    numbers = (1, 7, 22, 1524, 121.2350, -3.02)  # Примеры чисел для согласования с существительными.
    morph = MorphAnalyzer()
    word_ma = morph.parse(text)
    word_ma = word_ma[0]
    result = f'1й вариант нормальной формы для слова "{text}":\n'
    result += f'{word_ma.normal_form} - {word_ma.tag.cyr_repr}\n'

    # if len(word_ma) > 1:
    #     while not (n := input('Выберите вариант >> ')).isdecimal() or not 0 < int(n) <= len(word_ma):
    #         pass
    #     n = int(n) - 1
    # else:
    # n = 0

    word_lex = word_ma.lexeme

    if lex:
        result += f'\nСловоформы лексемы:\n'
        for i, word in enumerate(word_lex):
            result += f'{i + 1}: {word.word} - {word.tag.cyr_repr}\n'

    tag_str = str(word_ma.tag)
    if word_ma.tag.POS == 'NOUN' and not ('Pltm plur' in tag_str or 'Sgtm sing' in tag_str):
        word_ma = morph.parse(word_ma.normal_form)[0]
        word_gender = word_ma.tag.gender
        result += f'\nПримеры согласования нормальной формы слова "{text}" c числительными:\n'
        for i in numbers:
            num_text = n2w(i)
            # Если число вещественное (встречается фрагмент "цел"), изменить падеж слова на родительный.
            if 'цел' in num_text:
                word_ma = word_ma.inflect({'gent'})
                result += f'{i} -> {num_text} {word_ma.word}\n'
            else:
            # Если последнее слово "один" или "два", - согласовать его род с существительным.
                num_text = num_text.split()
                if (last_num_word := num_text[-1]) in ('один', 'два'):
                    last_num_word_ma = morph.parse(last_num_word)[0]
                    num_text[-1] = last_num_word_ma.inflect({word_gender}).word
                num_text = ' '.join(num_text)
                result += f'{i} -> {num_text} {word_ma.make_agree_with_number(i % 100).word}\n'
    return result


if __name__ == '__main__':
    print('Морфологический анализ слова на базе библиотеки pymorphy2')
    print('---------------------------------------------------------')
    while len(word := input('Введите слово >> ').strip()) == 0 or len(word.split()) > 1:
        print('Слово должно быть без пробелов и состоять минимум из 1 символа. Повторите ввод.')
    print(mt(word, True))
