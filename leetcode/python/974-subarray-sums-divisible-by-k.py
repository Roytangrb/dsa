# Author: RT
# Date: 2023-01-19T15:36:20.564Z
# URL: https://leetcode.com/problems/subarray-sums-divisible-by-k/


from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        prefix_remainder_count = Counter()
        prefix_remainder = 0
        prefix_remainder_count[0] += 1
        for num in nums:
            prefix_remainder = (prefix_remainder + num % k + k) % k
            ans += prefix_remainder_count[prefix_remainder]
            prefix_remainder_count[prefix_remainder] += 1

        return ans
