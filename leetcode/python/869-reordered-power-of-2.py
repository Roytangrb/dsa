# Author: RT
# Date: 2022-08-26T11:21:09.113Z
# URL: https://leetcode.com/problems/reordered-power-of-2/


from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = 1
        nums = []
        while num <= 1_000_000_000:
            nums.append(num)
            num <<= 1

        required = Counter(str(n))

        return any(num for num in nums if required == Counter(str(num)))
