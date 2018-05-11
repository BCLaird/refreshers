import sys
import unittest


def InsertionSort(nums):

    for i in range(0, len(nums)):
        num = nums[i]
        for j in range(0, i):
            if num < nums[j]:
                del nums[i]
                nums.insert(j, num)
                break

    return nums


class TestInsertionSort(unittest.TestCase):

    def test_min(self):
        self.assertEqual(InsertionSort([1]), [1])

    def test_reversed(self):
        unsorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(InsertionSort(unsorted), sorted)

    def test_front_half_sorted(self):
        unsorted = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(InsertionSort(unsorted), sorted)

    def test_back_half_sorted(self):
        unsorted = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(InsertionSort(unsorted), sorted)


if __name__ == "__main__":

    sys.stdout.write("Bryan Laird InsertionSort module.  Test mode.\n")
    sys.exit(unittest.main())
