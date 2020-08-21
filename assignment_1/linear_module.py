""" Linear/sequential searching """
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name


def linear_result_finder(tested_list, quarantined):
    """ The tested list contains (nhi, Name, result) tuples
        and isn't guaranteed to be in any order
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
    """
    comparisons = 0
    results = []
    # ---start student section---
    for q_name in quarantined:
        name_found = False
        for nhi, t_name, result in tested_list:
            comparisons += 1
            if q_name == t_name:
                results.append((q_name, nhi, result))
                name_found = True
                break
        if name_found is False:
            results.append((q_name, None, None))
    # ===end student section===
    return results, comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # write your own simple tests here
    # eg
    tested, quarantined, expected_results = [], [], []
    print("tested", tested)
    print("quarantine", quarantined)
    results, comparisons = linear_result_finder(tested, quarantined)
    print(results, comparisons)
