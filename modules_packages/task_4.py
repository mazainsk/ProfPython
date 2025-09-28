"""
Домашнее задание к лекции 1. «Import. Module. Package»
Задача 4
"""

from morphy_test import mt

words = ["роль", "слон", "нежность", "литр", "благо", "приятный"]

print('Морфологический анализ слова на базе библиотеки pymorphy2')
print('---------------------------------------------------------')

for i, word in enumerate(words):
    print(f'{i+1}. Cлово "{word}"', '-' * 20, sep='\n')
    print(mt(word))
