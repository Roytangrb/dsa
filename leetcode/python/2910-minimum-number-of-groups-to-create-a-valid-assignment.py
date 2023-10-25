# Author: RT
# Date: 2023-10-25T03:35:08.786Z
# URL: https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/description/


import math
from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, nums: list[int]) -> int:
        freq = Counter(nums)
        groups = list(freq.values())

        return min(
            result
            for split_size in range(1, min(groups) + 1)
            if (result := self.split_groups(split_size, groups)) != -1
        )

    def split_groups(self, split_size, groups):
        total = 0
        for group in groups:
            count, remainder = divmod(group, split_size)
            # when remainder <= number of partitions, we could
            # distribute the remainder to partitions so that each
            # partition has split_size of split_size + 1 elements
            if remainder > count:
                return -1

            # e.g. group = 12, split_size = 3, try to partition with
            # split_size + 1 = 4, to get smallest number of partitions
            # partitions are 3 3 3 3
            # when group = 13, partitions are 4 3 3 3
            # when group = 14, partitions are 4 4 3 3
            # when group = 15, partitions are 4 4 4 3
            # when group = 16, partitions are 4 4 4 4
            # when group = 17, partitions are 4 4 3 3 3
            # an extra partition is needed on every (split_size + 1) element
            total += math.ceil(group / (split_size + 1))

        return total
