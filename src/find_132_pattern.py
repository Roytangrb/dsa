"""https://leetcode.com/problems/132-pattern/"""


def find_132_pattern(nums: list[int]) -> bool:
    """Returns True if there exists i < j < k such that
    nums[i] < nums[k] < nums[j], otherwise False"""
    stack = []
    min_left = float("inf")

    for num in nums:
        # monotonically decreasing stack
        while stack and stack[-1][0] <= num:
            # update min value to the left of the current num
            min_left = min(min_left, stack.pop()[0])

        # if stack is not empty, nums[k] < nums[j] exists
        # check if the current num greater that min value
        # to the left of j, if so nums[k] < nums[i] exists
        if stack and num > stack[-1][1]:
            return True

        # store min value to the left of the current num
        stack.append((num, min_left))

    return False


if __name__ == "main":
    testcases = (
        ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        ([1, 0, 1, -4, -3], False),
    )

    for nums, expected in testcases:
        assert find_132_pattern(nums) == expected
