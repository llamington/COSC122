'''Compare search times with Python's inbuilt lists and sets.'''
import sys
import time
import random
# uncomment the following line to import matplotlib stuff
from matplotlib import pyplot


# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method

# define time.get_time to be the appropriate time counter
if sys.version_info < (3, 3):
    get_time = time.clock
    print("Using time.clock for timing - Python ver < 3.3")
else:
    get_time = time.perf_counter
    print("Using time.perf_counter for timing - Python ver >= 3.3")
    REZ = time.get_clock_info('perf_counter').resolution
    print('One unit of time is ' + str(REZ) + ' seconds')


def run_list_trials(num_trials=1):
    """ Creates lists filled with a range of values
    then searches for a randomly generated number in each list.
    Note: we are being nice here is that the number will be in the list...
    Returns two lists, the first contains all the list sizes tried and
    the second contains the average time per locate operation for each list size. """
    list_of_times = []
    # we will test for sizes [20000, 40000, 60000, etc...]
    list_of_sizes = list(range(20000, 1000001, 20000))
    for list_size in list_of_sizes:
        num_list = list(range(list_size))  # creates a list of n items

        # run trials, each on simply trying to locate the number in the list
        start = get_time()
        for i in range(num_trials):
            # try to find random number (between 1 and n) in the list
            value_to_find = random.randrange(list_size)
            found = value_to_find in num_list
        end = get_time()

        # print number of trials and time taken (with a tab in between)
        time_taken_per_locate = (end - start) / num_trials
        print(("{}\t{:>10.8f}" .format(list_size, time_taken_per_locate)))

        # keep track of all the times
        list_of_times.append(time_taken_per_locate)
    return list_of_sizes, list_of_times


def run_set_trials(num_trials=1):
    """ Creates a set and fills it with values,
    then searches for a randomly generated number in the set.
    Note: we are being nice here, as the number will be in the set..."""
    list_of_times = []
    list_of_sizes = list(range(20000, 1000001, 20000))
    for set_size in list_of_sizes:
        # fill test set with n items {0,1,2,....}
        test_set = {i for i in range(set_size)}

        # repeat the following num_trials times:
        start = get_time()
        for i in range(num_trials):
            # try to find random number (between 1 and n) in the list
            value_to_find = random.randrange(set_size)
            found = value_to_find in test_set
        end = get_time()
        # ===end student section===
        # keep track of all the times
        time_taken_per_locate = (end - start) / num_trials
        list_of_times.append(time_taken_per_locate)
    return list_of_sizes, list_of_times


def graph_one_series_example(n_trials):
    """An example of how to graph two series.
    IMPORTANT NOTE: Make sure the matplotlib import is uncommented
    at the top of this file before using this function
    """

    print('Getting list data for graph...')
    x1, y1 = run_list_trials(n_trials)
    pyplot.plot(x1, y1, 'bo')   # use blue o's as markers
    pyplot.title(f'List Locate Testing, {n_trials} Trial runs')
    pyplot.xlabel('n')
    pyplot.ylabel('Average Time per locate')
    pyplot.show()


def graph_two_series_example(n_trials):
    """An example of how to graph two series.
    IMPORTANT NOTE: Make sure the matplotlib import is uncommented
    at the top of this file before using this function
    """
    print('Getting list data for graph...')
    list_xs, list_ys = run_list_trials(n_trials)
    print()
    print('Getting set data for graph...')
    set_xs, set_ys = run_set_trials(n_trials)

    pyplot.plot(list_xs, list_ys, 'bo')  # use blue o's as markers
    pyplot.plot(set_xs, set_ys, 'ro')  # use red o's as markers
    pyplot.title(f'Locate Testing, {n_trials} Trial runs')
    pyplot.xlabel('n')
    pyplot.ylabel('Average Time per locate')
    pyplot.show()


def run_tests(n_trials):
    '''Function that runs various tests. Put your test calls in here'''

    print("LIST TRIAL RUN")
    print(f"Averages over {n_trials} trials.")
    print('size(n)\tAvg. Time')
    sizes, times = run_list_trials(n_trials)


def main():
    """ Put your tests in here """
    run_tests(n_trials=10)

    # uncomment either of the following lines to run some graphs

    # IMPORTANT NOTE: make sure you uncomment out the
    # import for matplotlib at the start of the file
    # before you start trying to do graph things
    graph_one_series_example(n_trials=10)
    graph_two_series_example(n_trials=10)
    #
    #
    # if you can't get matplotlib to run
    # then you can cut and paste the output from
    # run_tests into a spreadsheet, eg, Excel or Libre Office Calc
    # and do some graphing there


if __name__ == "__main__":
    main()
