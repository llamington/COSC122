"""Module containing the unit tests for the result getting functions."""
import signal
import os
import shutil
import tools
import unittest
import math
from classes import Name
from linear_module import linear_result_finder
from binary_module import binary_result_finder
from stats import IS_MARKING_MODE, NAME_COMPS, StatCounter
from tools import read_test_data, make_name_list

actual_count = StatCounter.get_count
lock_counter = StatCounter.lock_counter
unlock_counter = StatCounter.unlock_counter
DATA_DIR = './test_data/'


class BaseTester(unittest.TestCase):

    def setUp(self):
        """This runs before each test case"""
        unlock_counter(NAME_COMPS)
        StatCounter.reset_counts()
        # self.function_to_test should be setup by subclasses with the student function
        # that they want to test


    def AssertListsEqual(self, list1, list2):
        """ Locks the counter when comparing lists """
        lock_counter(NAME_COMPS)
        self.assertEqual(list1, list2)
        unlock_counter(NAME_COMPS)


class BaseTests(BaseTester):

    def get_bounds(self, left_length, right_length):
        raise NotImplementedError("This method should be "
                                  "implemented by a subclass.")

    def result_list_test(self, test_filename):
        test_file_location = DATA_DIR + test_filename
        tested, quarantined, expected_results = read_test_data(test_file_location)
        results, comparisons = self.function_to_test(tested, quarantined)
        self.AssertListsEqual(results, expected_results)
        self.assertEqual(type(results), type(expected_results))

    def comparisons_test(self, test_filename, expected_comparisons):
        test_file_location = DATA_DIR + test_filename
        tested, quarantined, expected_results = read_test_data(test_file_location)
        results, comparisons = self.function_to_test(tested, quarantined)
        self.assertEqual(comparisons, expected_comparisons)

    def internal_comparisons_test(self, test_filename):
        test_file_location = DATA_DIR + test_filename
        tested, quarantined, expected_results = read_test_data(test_file_location)
        results, comparisons = self.function_to_test(tested, quarantined)
        self.assertEqual(comparisons, actual_count(NAME_COMPS))

    def comparisons_within_bound_test(self, test_filename):
        test_file_location = DATA_DIR + test_filename
        tested, quarantined, expected_results = read_test_data(test_file_location)
        results, comparisons = self.function_to_test(tested, quarantined)
        lower_bound, upper_bound = self.get_bounds(len(tested),
                                                   len(quarantined),
                                                   len(results))
        self.assertGreaterEqual(comparisons, lower_bound)
        self.assertLessEqual(comparisons, upper_bound)




class TrivialListTest(BaseTests):

    def setUp(self):
        super().setUp()

    def test_single_result_small(self):
        filename = 'test_data-10n-10r-1-a.txt'
        self.result_list_test(filename)


class SmallTests(BaseTests):

    def setUp(self):
        super().setUp()

    def test_no_results_small(self):
        filename = 'test_data-10n-10r-0-a.txt'
        self.result_list_test(filename)

    # inherit this from TrivialListTest so don't need it again
    def test_single_results_small(self):
        filename = 'test_data-10n-10r-1-a.txt'
        self.result_list_test(filename)

    def test_10_results_small(self):
        filename = 'test_data-10n-10r-10-a.txt'
        self.result_list_test(filename)

    def test_no_results_small_comparisons_within_bound(self):
        filename = 'test_data-10n-10r-0-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_small_comparisons_within_bound(self):
        filename = 'test_data-10n-10r-1-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_10_results_small_comparisons_within_bound(self):
        filename = 'test_data-10n-10r-10-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_no_results_small_internal_comparisons(self):
        filename = 'test_data-10n-10r-0-a.txt'
        self.internal_comparisons_test(filename)

    def test_single_results_small_internal_comparisons(self):
        filename = 'test_data-10n-10r-1-a.txt'
        self.internal_comparisons_test(filename)

    def test_10_results_small_internal_comparisons(self):
        filename = 'test_data-10n-10r-10-a.txt'
        self.internal_comparisons_test(filename)


class MediumTests(BaseTests):

    def setUp(self):
        super().setUp()

    def test_no_results_medium(self):
        filename = 'test_data-50n-50r-0-a.txt'
        self.result_list_test(filename)

    def test_no_results_medium_comparisons_within_bound(self):
        filename = 'test_data-50n-50r-0-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_no_results_medium_internal_comparisons(self):
        filename = 'test_data-50n-50r-0-a.txt'
        self.internal_comparisons_test(filename)

    def test_single_results_medium(self):
        filename = 'test_data-50n-50r-1-a.txt'
        self.result_list_test(filename)

    def test_single_results_medium_comparisons_within_bound(self):
        filename = 'test_data-50n-50r-1-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_medium_internal_comparisons(self):
        filename = 'test_data-50n-50r-1-a.txt'
        self.internal_comparisons_test(filename)

    def test_10_results_medium_comparisons_within_bound(self):
        filename = 'test_data-50n-50r-10-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_10_results_medium(self):
        filename = 'test_data-50n-50r-10-a.txt'
        self.result_list_test(filename)

    def test_10_results_medium_internal_comparisons(self):
        filename = 'test_data-50n-50r-10-a.txt'
        self.internal_comparisons_test(filename)


class BigTests(BaseTests):

    def setUp(self):
        super().setUp()

    def test_no_results_big(self):
        filename = 'test_data-1000n-1000r-0-a.txt'
        self.result_list_test(filename)

    def test_no_results_big_comparisons_within_bound(self):
        filename = 'test_data-1000n-1000r-0-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_big(self):
        filename = 'test_data-1000n-1000r-1-a.txt'
        self.result_list_test(filename)

    def test_single_results_big_comparisons_within_bound(self):
        filename = 'test_data-1000n-1000r-1-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_big_internal_comparisons(self):
        filename = 'test_data-1000n-1000r-1-a.txt'
        self.internal_comparisons_test(filename)

    def test_10_results_big_comparisons_within_bound(self):
        filename = 'test_data-1000n-1000r-10-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_10_results_big(self):
        filename = 'test_data-1000n-1000r-10-a.txt'
        self.result_list_test(filename)

    def test_10_results_big_internal_comparisons(self):
        filename = 'test_data-1000n-1000r-10-a.txt'
        self.internal_comparisons_test(filename)


class HugeTests(BaseTests):

    def setUp(self):
        super().setUp()

    def test_no_results_huge(self):
        filename = 'test_data-10000n-10000r-0-a.txt'
        self.result_list_test(filename)

    def test_no_results_huge_comparisons_within_bound(self):
        filename = 'test_data-10000n-10000r-0-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_huge(self):
        filename = 'test_data-10000n-10000r-1-a.txt'
        self.result_list_test(filename)

    def test_single_results_huge_comparisons_within_bound(self):
        filename = 'test_data-10000n-10000r-1-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_huge_internal_comparisons(self):
        filename = 'test_data-10000n-10000r-1-a.txt'
        self.internal_comparisons_test(filename)

    def test_10_results_huge_comparisons_within_bound(self):
        filename = 'test_data-10000n-10000r-10-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_10_results_huge(self):
        filename = 'test_data-10000n-10000r-10-a.txt'
        self.result_list_test(filename)

    def test_10_results_huge_internal_comparisons(self):
        filename = 'test_data-10000n-10000r-10-a.txt'
        self.internal_comparisons_test(filename)


class GinormousTests(BaseTests):

    def setUp(self):
        super().setUp()

    def test_no_results_ginormous(self):
        filename = 'test_data-100000n-10000r-0-a.txt'
        self.result_list_test(filename)

    def test_no_results_ginormous_comparisons_within_bound(self):
        filename = 'test_data-100000n-10000r-0-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_ginormous(self):
        filename = 'test_data-100000n-10000r-1-a.txt'
        self.result_list_test(filename)

    def test_single_results_ginormous_comparisons_within_bound(self):
        filename = 'test_data-100000n-10000r-1-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_single_results_ginormous_internal_comparisons(self):
        filename = 'test_data-100000n-10000r-1-a.txt'
        self.internal_comparisons_test(filename)

    def test_10_results_ginormous_comparisons_within_bound(self):
        filename = 'test_data-100000n-10000r-10-a.txt'
        self.comparisons_within_bound_test(filename)

    def test_10_results_ginormous(self):
        filename = 'test_data-100000n-10000r-10-a.txt'
        self.result_list_test(filename)

    def test_10_results_ginormous_internal_comparisons(self):
        filename = 'test_data-100000n-10000r-10-a.txt'
        self.internal_comparisons_test(filename)


class BaseTestsLinear(BaseTests):

    def setUp(self):
        super().setUp()
        self.function_to_test = linear_result_finder

    def get_bounds(self, tested_size, quarantined_size, results_size):
        if tested_size < quarantined_size:
            lower_bound = tested_size * (tested_size - 1) / 2
        else:
            lower_bound = quarantined_size * (quarantined_size - 1) / 2
        upper_bound = tested_size * quarantined_size
        return lower_bound, upper_bound



# ------------------------------- Linear Tests ---------------------------------


class TrivialLinearTests(BaseTestsLinear, TrivialListTest):
    pass


class SmallLinearTests(BaseTestsLinear, SmallTests):

    # plus the following fixed comps checks
    def test_linear_no_results_small_comparisons_exact(self):
        # think about how we know this is 100
        filename = 'test_data-10i-10r-0-a.txt'
        self.comparisons_test(filename, 100)

    def test_linear_single_result_small_comparisons_exact(self):
        filename = 'test_data-10i-10r-1-a.txt'
        self.comparisons_test(filename, 94)

    def test_linear_two_results_small_comparisons_exact(self):
        filename = 'test_data-10i-10r-2-a.txt'
        self.comparisons_test(filename, 87)

    def test_linear_all_results_small_comparisons_exact(self):
        # think about how we know it's 55
        filename = 'test_data-10i-10r-10-a.txt'
        self.comparisons_test(filename, 55)


class BigLinearTests(BaseTestsLinear, BigTests):
    pass


class MediumLinearTests(BaseTestsLinear, MediumTests):
    pass


class HugeLinearTests(BaseTestsLinear, HugeTests):
    pass


class GinormousLinearTests(BaseTestsLinear, GinormousTests):
    pass


# ------------------------------- Binary Tests ---------------------------------
class BaseTestsBinary(BaseTests):

    def setUp(self):
        super().setUp()
        self.function_to_test = binary_result_finder

    def get_bounds(self, tested_size, quarantined_size, fraud_size):
        log2 = int(math.log(tested_size, 2))
        lower_bound = quarantined_size * (log2 + 1) - 2
        upper_bound = quarantined_size * (log2 + 2) + 2
        return lower_bound, upper_bound



class TrivialBinaryTests(BaseTestsBinary, TrivialListTest):
    pass


class SmallBinaryTests(BaseTestsBinary, SmallTests):
    pass


class MediumBinaryTests(BaseTestsBinary, MediumTests):
    pass


class BigBinaryTests(BaseTestsBinary, BigTests):
    pass


class HugeBinaryTests(BaseTestsBinary, HugeTests):
    pass


class GinormousBinaryTests(BaseTestsBinary, GinormousTests):
    pass


class TestTools(unittest.TestCase):
    """ Simple tests on tools.py """

    def setUp(self):
        StatCounter.reset_counts()

    def test_small_file_read(self):
        filename = 'test_data-10n-10r-0-a.txt'
        test_file_location = DATA_DIR + filename
        tested, quarantined, results = read_test_data(test_file_location)
        self.assertEqual(len(tested), 10)
        self.assertEqual(len(quarantined), 10)
        self.assertEqual(len(results), 10)
        number_with_results = 0
        for name, nhi, result in results:
            if result is not None:
                number_with_results += 1
        self.assertEqual(number_with_results, 0)
        self.assertEqual(0, actual_count(NAME_COMPS))

    def test_big_file_read(self):
        filename = 'test_data-10000n-10000r-10-a.txt'
        test_file_location = DATA_DIR + filename
        tested, quarantined, results = read_test_data(test_file_location)
        self.assertEqual(len(tested), 10000)
        self.assertEqual(len(quarantined), 10000)
        self.assertEqual(len(results), 10000)  # should be same as quarantined
        number_with_results = 0
        for name, nhi, result in results:
            if result is not None:
                number_with_results += 1
        self.assertEqual(number_with_results, 10)
        self.assertEqual(0, actual_count(NAME_COMPS))


class TestClasses(unittest.TestCase):
    """ Simple tests on things in classes.py """

    def setUp(self):
        StatCounter.reset_counts()

    def AssertListsEqual(self, voters1, voters2):
        """ Locks the counter when comparing voter lists """
        lock_counter(NAME_COMPS)
        self.assertEqual(voters1, voters2)
        unlock_counter(NAME_COMPS)

    def test_NameList_methods(self):
        test_list = NameList()
        self.assertEqual(len(test_list), 0)
        test_list.append(Name("Tim"))
        self.assertEqual(len(test_list), 1)
        test_list.append(Name("Paul"))
        self.assertEqual(len(test_list), 2)
        test_list.append(Name("Yalini"))
        self.assertEqual(len(test_list), 3)
        self.assertEqual(Name("Paul"), test_list[1])
        self.assertEqual(actual_count(NAME_COMPS), 1)
        self.AssertListsEqual(test_list, test_list)
        self.assertEqual(actual_count(NAME_COMPS), 1)
        to_compare = NameList()
        to_compare.append(Name("Tim"))
        to_compare.append(Name("Paul"))
        to_compare.append(Name("Yalini"))
        self.AssertListsEqual(test_list, to_compare)
        self.assertEqual(actual_count(NAME_COMPS), 1)
        self.assertEqual(len(test_list), 3)
# es


def all_tests_suite():
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TrivialLinearTests))
    # suite.addTest(unittest.makeSuite(SmallLinearTests))
    # suite.addTest(unittest.makeSuite(MediumLinearTests))
    # suite.addTest(unittest.makeSuite(BigLinearTests))
    # suite.addTest(unittest.makeSuite(HugeLinearTests))
    # suite.addTest(unittest.makeSuite(GinormousLinearTests))

    # uncomment the following lines when you're
    # ready to run such tests

    suite.addTest(unittest.makeSuite(TrivialBinaryTests))
    suite.addTest(unittest.makeSuite(SmallBinaryTests))
    suite.addTest(unittest.makeSuite(MediumBinaryTests))
    suite.addTest(unittest.makeSuite(BigBinaryTests))
    suite.addTest(unittest.makeSuite(HugeBinaryTests))
    suite.addTest(unittest.makeSuite(GinormousBinaryTests))

    # #suite.addTest(unittest.makeSuite(HelpfulDualTests))
    # #suite.addTest(unittest.makeSuite(TrivialDualTests))
    # #suite.addTest(unittest.makeSuite(SmallDualTests))
    # #suite.addTest(unittest.makeSuite(MediumDualTests))
    # #suite.addTest(unittest.makeSuite(BigDualTests))
    # #suite.addTest(unittest.makeSuite(HugeDualTests))
    # #suite.addTest(unittest.makeSuite(GinormousDualTests))
    # #suite.addTest(unittest.makeSuite(TrivialHashTableTests))
    # #suite.addTest(unittest.makeSuite(HashTableTests))
    # #suite.addTest(unittest.makeSuite(TrivialHashTests))
    # #suite.addTest(unittest.makeSuite(SmallHashTests))
    # #suite.addTest(unittest.makeSuite(MediumHashTests))
    # #suite.addTest(unittest.makeSuite(BigHashTests))
    # #suite.addTest(unittest.makeSuite(HugeHashTests))
    # #suite.addTest(unittest.makeSuite(GinormousHashTests))
    return suite




def main():
    """ Makes a test suite and runs it. Will your code pass? """
    test_runner = unittest.TextTestRunner(verbosity=2)
    all_tests = all_tests_suite()
    test_runner.run(all_tests)


if __name__ == '__main__':
    main()
