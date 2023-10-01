"""Quicksort"""


def sort_by_parity(nums: list[int]):
    """Move even num before odd num, similar to Lomuto partition in QuickSort.

    https://leetcode.com/problems/sort-array-by-parity/
    """
    n = len(nums)
    i = j = 0

    for j in range(n):
        if not nums[j] & 1:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


def test_sort_by_parity():
    testcases = (
        ([3, 1, 2, 4], [2, 4, 3, 1]),
        ([0], [0]),
    )
    for nums, expected in testcases:
        sort_by_parity(nums)
        assert nums == expected


if __name__ == "__main__":
    test_sort_by_parity()
