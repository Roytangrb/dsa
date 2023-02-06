# Author: RT
# Date: 2023-02-06T11:43:22.958Z
# URL: https://leetcode.com/problems/shuffle-the-array/


from itertools import chain


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return list(chain.from_iterable(zip(nums[:n], nums[n:])))
