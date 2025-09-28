
class Stack:
    """
    Класс для работы с объектами в виде стека из списка (очередь LIFO).

    """
    def __init__(self, except_errors=True, max_size=None):
        self.except_errors = except_errors
        self._data = []
        self._max_size = max_size

    def __str__(self):
        return (f'максимальный размер: {"не задан" if self._max_size is None else self._max_size}\n'
                f'элементов: {self.size()}\nсодержимое: {str(self._data)}')

    def __len__(self):
        return self.size()

    def is_empty(self):
        return not bool(self._data)

    def push(self, item):
        self._data.append(item)
        self._cut_max_size()

    def push_many(self, *args, **kwargs):
        for item in args:
            self._data.append(item)
        for key, value in kwargs.items():
            self._data.append((key, value))
        self._cut_max_size()

    def pop(self):
        if self._element_is_present():
            return self._data.pop()
        # return None здесь я не пишу, потому что оно и так вернется в нужном случае.

    def pop_many(self, count=None):
        if not self._element_is_present():
            return None
        if count is None:
            result_data = self._data
            self._data = []
        else:
            result_data = self._data[-count:]
            self._data[-count:] = []
        return result_data

    def peek(self):
        if self._element_is_present():
            return self._data[-1]

    def clear(self):
        self._data = []

    def size(self):
        return len(self._data)

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Размер стека должен быть целым положительным числом')
        self._max_size = value
        self._cut_max_size()

    def _element_is_present(self):
        if not self.is_empty():
            return True
        if self.except_errors:
            raise LookupError('Стек пустой')
        else:
            return False

    def _cut_max_size(self):
        if self._max_size is not None:
            self._data = self._data[-self._max_size:]
