# Author: RT
# Date: 2022-09-21T13:19:37.775Z
# URL: https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        ans = []
        esum = sum(num for num in nums if num % 2 == 0)
        for v, i in queries:
            # before adding query value, if num is even, it was accumlated to even sum
            # in previous step, subtract from sum first. After adding the query value
            # if num is still even, the new value is added to even sum.
            if nums[i] % 2 == 0:
                esum -= nums[i]

            nums[i] += v

            if nums[i] % 2 == 0:
                esum += nums[i]

            ans.append(esum)

        return ans
