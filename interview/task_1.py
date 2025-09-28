"""
Домашнее задание к лекции 7. «Подготовка к собеседованию»
Задача 1 (см. модуль stack)
"""

from stack import Stack

# Проверка работы со стеком.
my_stack = Stack(except_errors=False)
print(my_stack.is_empty())
print(my_stack.peek())  # При <except_errors=False> тут будет None

my_stack.push_many('a', ('b', 34), None, [188], z='False')
my_stack.push(str)  # Можно запихнуть любой объект, например, функцию.
print(my_stack)  # Работает dunder-метод __str__()
my_stack.push(55)
print(my_stack.pop_many(2))

# Работа с атрибутом объекта, определенным как свойство:
my_stack.max_size = 3  # Сеттер.
print(my_stack.max_size)  # Геттер.
print(my_stack)
print(len(my_stack))  # Работает dunder-метод __len__()
print(my_stack.is_empty())
