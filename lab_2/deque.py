import doctest
import os


class Deque(object):
    """
    Implements a Deque using a Python list internally.
    >>> d = Deque()
    >>> d.enqueue_front('a')
    >>> d.dequeue_front()
    'a'
    >>> d.enqueue_front('a')
    >>> d.enqueue_rear('b')
    >>> len(d)
    2
    >>> d.dequeue_rear()
    'b'
    >>> len(d)
    1
    """

    def __init__(self):
        self._data = []

    def enqueue_front(self, item):
        """Add an item onto the front of the deque."""
        self._data.insert(0, item)

    def enqueue_rear(self, item):
        """Add an item onto the rear of the deque."""
        self._data.append(item)

    def dequeue_front(self):
        """Remove an item from the front of the deque and return it."""
        if self.is_empty():
            raise IndexError("Can't dequeue_front from an empty deque!")
        else:
            # Not empty so remove front item and return it
            # ---start student section---
            return self._data.pop(0)
            # ===end student section===

    def dequeue_rear(self):
        """Remove an item from the rear of the deque and return it."""
        if self.is_empty():
            raise IndexError("Can't dequeue_rear from an empty deque!")
        else:
            # Not empty so remove rear item and return it
            # ---start student section---
            return self._data.pop(-1)
            # ===end student section===

    def is_empty(self):
        """ Returns True if the deque is empty."""
        return len(self._data) == 0

    def __len__(self):
        """ Returns the number of items in the deque."""
        return len(self._data)

    def __repr__(self):
        """ Returns a string representing the deque."""
        return "Front -> " + repr(self._data) + " <- Rear"


if __name__ == '__main__':
    # uncomment the following line if you have problems with strange characters
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h

    # failed doctests will show you what you need to fix/write
    # If everything works then the doctests will output nothing...
    doctest.testmod()

    d = Deque()  # make q an empty deque
    d.enqueue_front(13)
    d.enqueue_rear(29)
    d.enqueue_rear(24)
    a = d.dequeue_front()
    b = d.dequeue_front()
    d.enqueue_front(30)
    d.enqueue_rear(17)
    d.enqueue_rear(21)
    c = d.dequeue_front()

    print(a)
    print(b)
    print(c)