# Author: RT
# Date: 2023-03-04T16:25:28.865Z
# URL: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        """O(n) - Scan num from left to right, keep track of 3 things
        1. right-most out of bound index
        2. right-most lower bound index
        3. right-most upper bound index
        sum number of fixed bound sub-arrays ending at each index
        """
        out_of_bound = lower_bound = upper_bound = -1
        ans = 0
        for r, num in enumerate(nums):
            if num < minK or num > maxK:
                out_of_bound = r
                continue
            if num == minK:
                lower_bound = r
            if num == maxK:
                upper_bound = r

            # sub-array must include the most recent of both bounds
            l = min(lower_bound, upper_bound)
            ans += max(l - out_of_bound, 0)

        return ans

    def brute_force(self, nums: list[int], minK: int, maxK: int) -> int:
        # O(n2)
        n = len(nums)
        ans = 0
        for l in range(n):
            w_min = w_max = nums[l]
            for r in range(l, n):
                w_min = min(w_min, nums[r])
                w_max = max(w_max, nums[r])
                if w_min == minK and w_max == maxK:
                    ans += 1
                if w_min < minK or w_max > maxK:
                    break

        return ans
