"""
Домашнее задание к лекции 3. «Decorators»
Задача 3. Применение логгера из задачи 2 к задачам из предыдущих домашних заданий.
"""

import os
from regexp.main import phonebook_processing as pp
from task_2 import logger
from modules_packages.morphy_test import mt

def task_3():
    path = 'task_3.log'
    if os.path.exists(path):
        os.remove(path)

    @logger(path)
    def phonebook_data_processing():
        return pp()

    @logger(path)
    def word_morphy():
        words = ["роль", "слон", "нежность", "литр", "благо", "приятный"]
        result = ''
        for i, word in enumerate(words):
            result += f'\n{i+1}. Cлово "{word}"\n--------------------\n'
            result += mt(word)
        return result

    phonebook_data_processing()
    word_morphy()


if __name__ == '__main__':
    task_3()
