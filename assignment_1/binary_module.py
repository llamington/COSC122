""" Binary search is trickier than you think.
Remember your binary search should only use one comparison
per while loop, ie, one comparison per halving.
"""

import tools
# uncomment the next line if you want to make some Name objects
from classes import Name

# We recomment using a helper function that does a binary search
# for a Name in a given tested list. This will let you test your
# binary search by itself.




def binary_result_finder(tested, quarantined):
    """ The tested list contains (nhi, Name, result) tuples and
        will be sorted by Name
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the  quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
        Note: You shouldn't sort the tested_list, it is already sorted. Sorting it
        will use lots of extra comparisons!
    """
    total_comparisons = 0
    results = []
    # ---start student section---
    for q_name in quarantined:
        lower_bound = 0
        upper_bound = len(tested) - 1
        while lower_bound < upper_bound:
            middle_index = lower_bound + (upper_bound - lower_bound) // 2
            test = tested[middle_index]
            total_comparisons += 1
            if test[1] < q_name:
                lower_bound = middle_index + 1
            else:
                upper_bound = middle_index
        test = tested[lower_bound]
        total_comparisons += 1
        if test[1] == q_name:
            results.append((test[1], test[0], test[2]))
        else:
            results.append((q_name, None, None))
    # ===end student section===
    return results, total_comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # feel free to do some of your simple tests here
    # eg,
    filename = "test_data/test_data-50n-50r-50-a.txt"
    tested, quarantined, expected_results = [(2120073, Name('Austin Alfred'), True)], [Name('Austin Alfred')], [(Name('Austin Alfred'), 2120092, True)]
    results, comparisons = binary_result_finder(tested, quarantined)
    # print(quarantined)
    # print(tested)
    print(results, comparisons)
    print(expected_results)
