import sys
import unittest


def merge(nums1, nums2):
    """
    :param nums1: Sorted list of numbers.
    :param nums2: Sorted list of numbers.
    :return: Combined sorted list of numbers.
    """

    merged = list()

    while len(nums1) != 0 and len(nums2) != 0:
        if nums1[0] < nums2[0]:
            merged.append(nums1.pop(0))
        else:
            merged.append(nums2.pop(0))

    while len(nums1) != 0:
        merged.append(nums1.pop(0))

    while len(nums2) != 0:
        merged.append(nums2.pop(0))

    return merged


def merge_sort(nums):
    """
    :param nums: List of numbers to sort.
    :return: Sorted list of  numbers.
    """

    if len(nums) != 1:
        nums1 = merge_sort(nums[:(len(nums) / 2)])
        nums2 = merge_sort(nums[(len(nums) / 2):])
        sorted_nums = merge(nums1, nums2)
        return sorted_nums
    else:
        # Nothing to do for a list of length 1.
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
