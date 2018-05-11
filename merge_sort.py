import os
import sys
import unittest


def merge_sort(nums):

    if len(nums) != 1:
        pass

    return nums


class TestInsertionSort(unittest.TestCase):

    def test_min(self):
        self.assertEqual([1], merge_sort([1]))

    def test_reversed(self):
        unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, merge_sort(unsorted))

    def test_front_half_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, merge_sort(unsorted))

    def test_back_half_sorted(self):
        unsorted = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, merge_sort(unsorted))


if __name__ == "__main__":

    sys.stdout.write("Bryan Laird merge_sort module.  Test mode.\n")
    sys.exit(unittest.main())