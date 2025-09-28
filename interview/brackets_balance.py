
from stack import Stack


def check_balance(brackets: str) -> bool:
    if len(brackets) % 2 != 0:
        return False

    open_brackets = '({['
    close_brackets = ')}]'
    my_stack = Stack()

    for item in brackets:
        if item in open_brackets:
            my_stack.push(item)
            continue

        if item not in close_brackets:
            return False

        if my_stack.is_empty():
            return False

        last_open = my_stack.pop()
        if close_brackets.find(item) != open_brackets.find(last_open):
            return False
    return True
