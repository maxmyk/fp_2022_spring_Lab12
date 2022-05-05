"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    >>> queue = ArrayQueue()
    >>> for i in range(10): queue.add(i)
    >>> stack = queue_to_stack(queue)
    >>> print(queue)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> print(stack)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> print(stack.pop())
    0
    >>> print(queue.pop())
    0
    >>> stack.add(11)
    >>> queue.add(11)
    >>> print(queue)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    >>> print(stack)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
    """
    new_stack = ArrayStack()
    orig_queue = ArrayQueue()
    orig_queue._front = queue._front
    orig_queue._rear = queue._rear
    orig_queue._items = queue._items
    orig_queue._size = queue._size
    to_add = [orig_queue.pop() for _ in range(queue._size)]
    for elem in to_add[::-1]:
        new_stack.add(elem)
    return new_stack

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
