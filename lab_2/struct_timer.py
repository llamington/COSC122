import sys
import random
import time
from stack import Stack
from queue122 import Queue
from deque import Deque


# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method
# define get_time to be the appropriate time counter
if sys.version_info < (3, 3):
    get_time = time.clock
    print("Using time.clock for timing - Python ver < 3.3")
else:
    get_time = time.perf_counter
    print("Using time.perf_counter for timing - Python ver >= 3.3")
    REZ = time.get_clock_info('perf_counter').resolution
    print('Smallest unit of time is ' + str(REZ) + ' seconds')


def time_stack_push(initial_size, n_trials):
    """ Finds average time for pushing onto a stack of a given initial size"""
    s = Stack()

    # s._data = [0] * initial_size  # is cunning but sometimes causes weird timings
    # so simply push lots of random items onto the stack
    for _ in range(initial_size):
        s.push(random.randint(0, 127))

    # time some pushes
    start_time = get_time()
    for i in range(n_trials):
        s.push(0)
    end_time = get_time()
    time_per_operation = (end_time - start_time)/n_trials
    template = "Initial Stack size = {:,d} -> avg. time/push for {:,d} pushes is {:10.8f}"
    print((template.format(initial_size, n_trials, time_per_operation)))


# Do some creative copy and pasting here to make functions for other time trials
# ---start student section---

# ===end student section===


def run_tests():
    """ Runs as many or as few tests as you call,
    initially just runs the test for stack pushes
    """
    print('\n' *3)
    initial_size = 1000000  # start with this many items in data structure
    n_trials = 100  # run this many trials and take the average time

    time_stack_push(initial_size, n_trials)
    # call your shiny new test functions here


run_tests()
