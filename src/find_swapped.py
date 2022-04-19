"""Find two swapped elements in a sorted array

https://leetcode.com/problems/recover-binary-search-tree/
"""


def find_two_swapped(nums: list[int]) -> tuple[int, int]:
    """Return indices of the two swapped elements"""
    n = len(nums)
    x = y = -1
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            y = i

            # first occurrence, nums[i - 1] is the large value moved to front
            if x == -1:
                x = i - 1
            # second occurrence, nums[i] is the small value swapped to back
            else:
                break

    return x, y


def test_find_two_swapped():
    testcases = (
        ([2, 1], (0, 1)),
        ([1, 3, 2, 4], (1, 2)),
        ([1, 4, 3, 2, 5], (1, 3)),
    )

    for arr, expected in testcases:
        assert (actual := find_two_swapped(arr)) == expected, f"{expected=}, {actual=}"


if __name__ == "__main__":
    test_find_two_swapped()
