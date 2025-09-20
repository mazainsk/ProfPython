# pip install pymorphy2
# pip install num2words
# Версия Python должна быть не выше 3.10

from pymorphy2 import MorphAnalyzer
from n2w import n2w

numbers = (1, 7, 22, 1524, 121.2350, -3.02)  # Примеры чисел для согласования с существительными.
morph = MorphAnalyzer()
print('Морфологический анализ слова на базе библиотеки pymorphy2')
print('---------------------------------------------------------')
while len(text := input('Введите слово >> ').strip()) == 0 or len(text.split()) > 1:
    print('Слово должно быть без пробелов и состоять минимум из 1 символа. Повторите ввод.')
word_ma = morph.parse(text)
word_ma = word_ma[:2]  # Ограничиваюсь первыми двумя вариантами.
print()
print('Варианты нормальных форм:')
for i, word in enumerate(word_ma):
    print(f'{i + 1}: {word.normal_form} - {word.tag.cyr_repr}')
print()
if len(word_ma) > 1:
    while not (n := input('Выберите вариант >> ')).isdecimal() or not (0 < int(n) <= len(word_ma)):
        pass
    n = int(n) - 1
else:
    n = 0
word_lex = word_ma[n].lexeme
print('Словоформы лексемы:')
for i, word in enumerate(word_lex):
    print(f'{i + 1}: {word.word} - {word.tag.cyr_repr}')
tag_str = str(word_ma[n].tag)
if word_ma[n].tag.POS == 'NOUN' and not ('Pltm plur' in tag_str or 'Sgtm sing' in tag_str):
    word_ma = morph.parse(word_ma[n].normal_form)[0]
    word_gender = word_ma.tag.gender
    print()
    print('Согласование нормальной формы слова c числительными:')
    for i in numbers:
        num_text = n2w(i)
        # Если число вещественное (встречается фрагмент "цел"), то нужно изменить падеж слова на родительный.
        if 'цел' in num_text:
            word_ma = word_ma.inflect({'gent'})
            print(i, '->', num_text, word_ma.word)
        else:
        # Если последнее слово "один" или "два", нужно согласовать его род с существительным.
            num_text = num_text.split()
            if (last_num_word := num_text[-1]) in ('один', 'два'):
                last_num_word_ma = morph.parse(last_num_word)[0]
                num_text[-1] = last_num_word_ma.inflect({word_gender}).word
            num_text = ' '.join(num_text)
            print(i, '->', num_text, word_ma.make_agree_with_number(i % 100).word)
