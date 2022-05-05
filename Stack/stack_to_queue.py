"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    >>> stack = ArrayStack()
    >>> for i in range(10): stack.add(i)
    >>> queue = stack_to_queue(stack)
    >>> print(queue)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> print(stack)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(stack.pop())
    9
    >>> print(queue.pop())
    9
    >>> stack.add(11)
    >>> queue.add(11)
    >>> print(queue)
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    >>> print(stack)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
    """
    orig_stack = ArrayStack()
    new_queue = ArrayQueue()
    for elem in stack:
        orig_stack.push(elem)
    to_add = [orig_stack.pop() for _ in range(orig_stack._size)]
    for elem in to_add:
        new_queue.add(elem)
    return new_queue


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
