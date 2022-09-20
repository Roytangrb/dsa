# Author: RT
# Date: 2022-09-20T14:43:16.527Z
# URL: https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)

        ans = 0
        # dp[i][j] longest common subarray starting at nums1[i] and nums2[j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    ans = max(ans, dp[i][j])

        return ans

    # Sliding window approach O(mn)
    # slide the smaller array onto the larger array, 1 index offset each time
    # keep track of counts of consecutive matches in each overlap window
    # e.g.
    # ---
    #    [1, 2, 3]
    #          [2, 3]
    # ---
    #    [1, 2, 3]
    #       [2, 3]
    # ---
    #    [1, 2, 3]
    #    [2, 3]
    # ---
    #    [1, 2, 3]
    # [2, 3]
    # every start position pairs in nums1 and nums2 are taken into account
