import doctest
import os


class Stack(object):
    """Provides a stack with associated stack opertations.
    Internally the stack is stored as plain Python list.
    The top of the stack is at _data[n] and the bottom is at _data[0]
    _data is a private variable inside each stack instance and shouldn't
    be accessed from outside the stack (eg, don't do s._data.pop(), you should
    be using s.pop()

    >>> s = Stack()
    >>> s.push('a')
    >>> s.peek()
    'a'
    >>> s.pop()
    'a'
    >>> s.push('a')
    >>> s.push('b')
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> s.pop()
    'b'
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack!
    >>> print(s.peek())
    None
    """

    def __init__(self):
        self._data = []

    def push(self, item):
        """Push a new item onto the stack."""
        # ---start student section---
        self._data.append(item)
        # ===end student section===

    def pop(self):
        """ Pop an item off the top of the stack and return it.
        Python has a method to remove and return the last item
        from a list, can you guess what it is?
        Raise IndexError if empty - see comments below.
        """
        if self.is_empty():
            raise IndexError('Can\'t pop from empty stack!')
        else:
            # not empty so write your code to remove the last
            # item from the data list and return it
            # ---start student section---
            return self._data.pop()
            # ===end student section===

    def peek(self):
        """Return the item on the top of the stack, but don't remove it.
        Returns None if the list is empty
        """
        # ---start student section---
        return self._data[-1] if not self.is_empty() else None
        # ===end student section===

    def is_empty(self):
        """ Returns True if empty """
        return len(self._data) == 0

    def __len__(self):
        """ Returns the number of items in the stack """
        return len(self._data)

    def __str__(self):
        """ Returns a nice string representation of the Stack """
        return "Bottom -> " + repr(self._data) + " <- Top"

    def __repr__(self):
        """ Returns a representation, simply the __str__
        This is useful for displaying the Stack in the shell
        """
        return str(self)


if __name__ == '__main__':
    # uncomment the following line if you have problems with strange characters
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h

    # failed doctests will show you what you need to fix/write
    # If everything works then the doctests will output nothing...
    doctest.testmod()

    # These are the same as the doctests provided
    s = Stack()
    # make s an empty Stack
    s.push(37)
    s.push(18)
    a = s.pop()
    s.push(29)
    s.push(33)
    b = s.pop()
    s.push(36)
    s.push(20)
    s.push(41)
    c = s.pop()

    print(a)
    print(b)
    print(c)