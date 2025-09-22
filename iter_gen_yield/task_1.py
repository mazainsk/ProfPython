"""
Домашнее задание к лекции 2. «Iterators. Generators. Yield»
Задача 1

"""

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor_list = 0
        self.cursor_item = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor_item += 1
        if self.cursor_item >= len(self.list_of_list[self.cursor_list]):
            self.cursor_item = 0
            self.cursor_list += 1
            if self.cursor_list >= len(self.list_of_list):
                raise StopIteration
        return self.list_of_list[self.cursor_list][self.cursor_item]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
