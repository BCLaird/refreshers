import sys
import unittest


def quick_sort(nums):
    """
    :param nums: List of numbers to sort.
    :return: Sorted list of  numbers.
    """

    if len(nums) == 0:
        return nums
    else:
        pivot = nums[-1]

        left = list()
        right = list()
        for i in range(len(nums) - 1):
            if nums[i] <= pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        left_sorted = quick_sort(left)
        right_sorted = quick_sort(right)

        sorted_nums = left_sorted + [pivot] + right_sorted

        return sorted_nums


class TestInsertionSort(unittest.TestCase):

    def test_one(self):
        self.assertEqual([1], quick_sort([1]))

    def test_two(self):
        unsorted = [2, 1]
        sorted = [1, 2]
        self.assertEqual(sorted, quick_sort(unsorted))

    def test_three(self):
        unsorted = [2, 3, 1]
        sorted = [1, 2, 3]
        self.assertEqual(sorted, quick_sort(unsorted))

    def test_reversed(self):
        unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, quick_sort(unsorted))

    def test_front_half_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, quick_sort(unsorted))

    def test_back_half_sorted(self):
        unsorted = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sorted, quick_sort(unsorted))


if __name__ == "__main__":

    sys.stdout.write("Bryan Laird quick_sort module.  Test mode.\n")
    sys.exit(unittest.main())
