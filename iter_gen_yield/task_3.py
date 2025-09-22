"""
Домашнее задание к лекции 2. «Iterators. Generators. Yield»
Задача 3

"""

class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.flat_list = []
        self._flatten(self.nested_list)
        self.index = 0

    def _flatten(self, nested):
        """ Функция рекурсивно формирует из вложенных списков плоский список в атрибуте класса. """
        for item in nested:
            if isinstance(item, list):
                self._flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration
        value = self.flat_list[self.index]
        self.index += 1
        return value

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()