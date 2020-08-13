from random import *
from turtle import *


class Node:

    def __init__(self, item):
        self.item = item
        self.next_node = None


def add_item_to_list(first_node, item):
    """
    Adds item to end of linked list.
    first_node is the first node in the list.
    Note: this is a non-recursive function
    To help us build lists for testing.
    Think about how to make it recursive :)
    """
    if first_node is None:
        # the list needs a first node
        # initialise a first node with first_node = Node(item)
        # then call add_item_to_list to add another node
        raise IndexError("None doesn't have a .next_node")
    else:
        new_node = Node(item)
        current_node = first_node
        # traverse list until at last node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        # set last node's next pointer to point to the new node
        current_node.next_node = new_node


def gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a - b, b)


def str_length(s):
    """
    Calculates the length of a string.
    Definitely not the best way of doing this!
    Think about how much space all the sub lists will take up.
    """
    if s == "":
        return 0
    return 1 + str_length(s[1:])


def fib_recursive(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_recursive(0)
    0
    >>> fib_recursive(1)
    1
    >>> fib_recursive(2)
    1
    >>> fib_recursive(3)
    2
    >>> fib_recursive(4)
    3
    >>> fib_recursive(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_iterative(0)
    0
    >>> fib_iterative(1)
    1
    >>> fib_iterative(2)
    1
    >>> fib_iterative(3)
    2
    >>> fib_iterative(4)
    3
    >>> fib_iterative(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n_minus2 = 0
        fib_n_minus1 = 1      # start with fib of 2 which equals 1
        for i in range(1, n):  # there will be n+1 numbers including the 0'th
            curr_fib = fib_n_minus1 + fib_n_minus2
            fib_n_minus2 = fib_n_minus1
            fib_n_minus1 = curr_fib
        return curr_fib


def fibonacci_sequence(n):
    """
    Prints Fibonacci numbers up to the nth number (including the 0th number).

    >>> fibonacci_sequence(9)
    0 1 1 2 3 5 8 13 21 34
    """
    if n == 0:
        print(0, end='')
    else:
        fibonacci_sequence(n - 1)
        print(' ' + str(fib_recursive(n)), end='')


def tree(size, level):
    """
     Draws a funky fractal tree.
     Feel free to experiment with parameters...
     """
    if level != 0:
        forward(random() * size)
        x = pos()
        angle = random() * 20
        right(angle)
        tree(size * .8, level - 1)
        setpos(x)
        left(angle)
        angle = random() * -20
        right(angle)
        tree(size * .8, level - 1)
        left(angle)
        setpos(x)


#-------------------------------------------------------------------------
# Functions for students to implement
#-------------------------------------------------------------------------


# -------------- power to the recursionists! -----------------------------

def slow_power(x, n):
    """Computes x to the power of n, the slow way!
    Named slow_power to distinguish it from quick_power, which you will write later.
    >>> slow_power(2, 2)
    4
    >>> slow_power(2, 3)
    8
    """
    if n == 0:
        return 1
    else:
        return x * slow_power(x, n - 1)


def quick_power(x, n):
    """
    Computes x ^ n where n is an integer and is >= 0
    Feel free to raise an exception if n is not valid.
    NOTES:
    - You need to write the doc test for the base case.
    - You shouldn't use the ** operator in your function
    - You shouldn't use the low_power function either
    - Remember n squared is simply n * n
        + quick_power should only call itself once...
    >>> quick_power(2,3)
    8
    >>> quick_power(2,8)
    256
    >>> quick_power(2,16)
    65536

    """
    # ---start student section---
    if n == 0:
        return 1
    elif n % 2 == 0:
        sqrt_ans = quick_power(x, n/2)
        return sqrt_ans * sqrt_ans
    else:
        return x * quick_power(x, n-1)
    # ===end student section===


def factorial(n):
    """
    Returns n!

    n must be >= 0
    Feel free to raise an exception if n is not valid.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    # ---start student section---
    pass
    # ===end student section===


# -------------- Recursive linked lists ----------------------

def linked_list_length(list_node):
    """
    Returns the number of nodes in a linked list,
    0 if list is empty.

    >>> first_node = Node(1)
    >>> linked_list_length(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_length(first_node)
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_length(first_node)
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_length(first_node)
    4
    >>> add_item_to_list(first_node, 10)
    >>> linked_list_length(first_node)
    5
    """
    # Note: you shouldn't be using a while loop here.
    # Think of the length of the list as the length of
    # the first node (ie 1) plus the length of the rest of the list.
    # Remember you should be using recursion so your function should
    # call linked_list_length at some stage!
    # ---start student section---
    if list_node is None:
        return 0
    else:
        return 1 + linked_list_length(list_node.next_node)
    # ===end student section===


def linked_list_print(list_node):
    """
    Prints list, one item per line.

    >>> first_node = Node(1)
    >>> linked_list_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_print(first_node)
    1
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_print(first_node)
    1
    2
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_print(first_node)
    1
    2
    3
    4
    """
    # Note: you shouldn't be using a while loop here.
    # Remember you should be using recursion so your function should
    # call linked_list_print at some stage!
    # ---start student section---
    if list_node is None:
        return None
    else:
        print(list_node.item)
        linked_list_print(list_node.next_node)
    # ===end student section===


def linked_list_reverse_print(list_node):
    """
    Prints list in reverse, one item per line.

    >>> first_node = Node(1)
    >>> linked_list_reverse_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_reverse_print(first_node)
    2
    1
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_reverse_print(first_node)
    3
    2
    1
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_reverse_print(first_node)
    4
    3
    2
    1
    """
    # Note: you shouldn't be using a while loop here.
    # Remember you should be using recursion so your function should
    # call linked_list_reverse_print at some stage!
    # Hint: make sure you aren't calling linked_list_print!
    # ---start student section---
    if list_node.next_node is None:
        print(list_node.item)
    else:
        linked_list_reverse_print(list_node.next_node)
        print(list_node.item)

    # ===end student section===


def is_in_linked_list(list_node, item):
    """
    Returns TRUE if item is in list, otherwise False.

    >>> first_node = Node(1)
    >>> is_in_linked_list(first_node,2)
    False
    >>> add_item_to_list(first_node, 2)
    >>> is_in_linked_list(first_node,2)
    True
    >>> add_item_to_list(first_node, 3)
    >>> add_item_to_list(first_node, 4)
    >>> add_item_to_list(first_node, 5)
    >>> is_in_linked_list(first_node,3)
    True
    >>> is_in_linked_list(first_node,10)
    False
    """
    # Note: you shouldn't be using a while loop here.
    # An item is in the list if it is in the list_node or in the rest of the list
    # The base case is when list_node is None (what should you return in this case?).
    # Remember you should be using recursion so your function should
    # call is_in_linked_list at some stage!
    # ---start student section---
    if list_node is None:
        return False
    else:
        if list_node.item == item:
            return True
        else:
            return is_in_linked_list(list_node.next_node, item)
    # ===end student section===


# -------------- Recursion with Python lists and strings -----------------
def recursive_string_print(s):
    """
    Prints a string out, one character per line, using recursion
    Think about why this is very inefficient for long strings!
    >>> recursive_string_print('blah')
    b
    l
    a
    h
    >>> recursive_string_print('pi')
    p
    i
    """
    # ---start student section---
    if len(s) != 0:
        print(s[0])
        recursive_string_print(s[1:])
    # ===end student section===


def recursive_reverse_string_print(s):
    """
    Prints a string out in reverse, one character per line, using recursion
    Feel free to use list slicing - but do think about why this is very
    inefficient for long strings!
    >>> recursive_reverse_string_print('blah')
    h
    a
    l
    b
    >>> recursive_reverse_string_print('pi')
    i
    p
    """
    # ---start student section---
    if len(s) != 0:
        print(s[-1])
        recursive_reverse_string_print(s[:-1])
    # ===end student section===


def squares(data):
    """ A recursive function that takes a list of ints
    and returns a list with the squares of those values.
    The function shouldn't change the original data list.
    Feel free to use list slicing here.
    You shouldn't use list comprehensions, as it would
    effectively be reverting to simple iteration
    >>> squares([1,2,3,4,5])
    [1, 4, 9, 16, 25]
    >>> squares([10,20,30,40])
    [100, 400, 900, 1600]
    >>> squares([1])
    [1]
    >>> squares([-11])
    [121]
    >>> data = list(range(1,11))
    >>> squares(data)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> data
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # ---start student section---
    if len(data) != 0:
        previous_return = squares(data[1:])
        if previous_return:
            return [data[0] ** 2] + previous_return
        else:
            return [data[0] ** 2]
    else:
        return []

    # ===end student section===


def nice_recursive_string_print(string, index=0):
    """
    Prints a string out, one character per line, staring at index.
    Does so without having to make substring copies, ie, no string slicing.
    By string slicing we mean expressions such as string[1:]
    >>> nice_recursive_string_print('blah')
    b
    l
    a
    h
    >>> nice_recursive_string_print('pi')
    p
    i
    >>> nice_recursive_string_print('zippy', 2)
    p
    p
    y
    """
    # ---start student section---
    if len(string) > index:
        print(string[index])
        nice_recursive_string_print(string, index + 1)
    # ===end student section===


def rec_list_print(alist, start_index=0):
    if start_index < len(alist):
        print(alist[start_index])
        rec_list_print(alist, start_index + 1)


# ------------------- Just in case you were missing Herbert --------------

def num_rushes(slope_height, rush_height_gain, back_sliding, start_height=0):
    """Herbert again, recursively this time.
    Herbert the Heffalump is trying to climb up a scree slope. He finds that the
    best approach is to rush up the slope until he's exhausted, then pause to
    get his breath back. However, while he pauses each time, the slope settles
    underneath him, carrying him back down part of the slope he just climbed.
    This function calculates how many rushes it takes Herbert to climb up a
    slope of height slope_height metres, given that each rush gains him
    rush_height_gain metres before he slides back back_sliding metres during the
    pause before the next rush. If a rush gets him to the slope height or higher
    then Herbert won't back slide. The final rush will still be counted as one
    rush, even though it may be of shorter duration than the previous rushes.
    This implementation of num_rushes must be written without any loops,
    import statements, or list comprehensions.
    >>> num_rushes(10, 10, 9)
    1
    >>> num_rushes(100, 10, 0)
    10
    >>> num_rushes(15, 10, 5)
    2
    >>> num_rushes(100, 15, 7)
    12
    >>> num_rushes(200, 16, 9)
    28
    """
    # ---start student section---
    if slope_height <= start_height:
        return 0
    elif start_height + rush_height_gain >= slope_height:
        return 1
    else:
        return 1 + num_rushes(slope_height, rush_height_gain, back_sliding, start_height+rush_height_gain-back_sliding)
    # ===end student section===


if __name__ == '__main__':
    # These imports are here to save you stress when submitting functions
    # to the quiz server. Normally they would go at the start of the module.
    import doctest
    import os
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h

    # Comment out the next line if you want to run individual tests
    doctest.testmod()

    # then uncomment individual doctest runs below
    #doctest.run_docstring_examples(slow_power, None)
    #doctest.run_docstring_examples(quick_power, None)
    #doctest.run_docstring_examples(factorial, None)

    #doctest.run_docstring_examples(linked_list_length, None)
    #doctest.run_docstring_examples(linked_list_print, None)
    #doctest.run_docstring_examples(linked_list_reverse_print, None)
    #doctest.run_docstring_examples(is_in_linked_list, None)

    #doctest.run_docstring_examples(recursive_string_print, None)
    #doctest.run_docstring_examples(recursive_reverse_string_print, None)
    #doctest.run_docstring_examples(squares, None)

    #doctest.run_docstring_examples(nice_recursive_string_print, None)
    #doctest.run_docstring_examples(rec_print_list, None)
    #doctest.run_docstring_examples(num_rushes, None)

    # Some other interesting tests to run:
    # -----------------------------------
    #n = 5000
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    # print('\n')

    #n = 100
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    # print('\n')

    #n = 31
    #print('fib({0:d}) = {1:d}'.format(n,fib_recursive(n)))
    # print('\n')

    # Given the value for fib_iterative(100) would it be wise
    # to try to run fib_recursive(100)????

    #my_list = Node('b')
    #add_item_to_list(my_list, 'a')
    # linked_list_print(my_list)
