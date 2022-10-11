# Author: RT
# Date: 2022-10-11T13:24:59.558Z
# URL: https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        prefix_min = [float("inf")] * n
        for i in range(n - 1):
            prefix_min[i + 1] = min(prefix_min[i], nums[i])

        suffix_max = nums[-1]
        for i in range(n - 2, -1, -1):
            if prefix_min[i] < nums[i] < suffix_max:
                return True

            suffix_max = max(suffix_max, nums[i])

        return False

    def increasingTriplet__one_pass(self, nums: list[int]) -> bool:
        # It's possible that first_num is not in the subsequence. It's ok to update
        # first_num to a even smaller value when second_num has not been updated yet.
        # first_num is the samller, triplet is possible if we always update first_num first.
        # Example: [1, 2, 0, 3]

        first_num = float("inf")
        second_num = float("inf")

        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True

        return False
