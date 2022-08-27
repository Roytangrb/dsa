# Author: RT
# Date: 2022-08-27T19:11:59.844Z
# URL: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

# Maximum Sum Rectangular Submatrix:
# https://www.youtube.com/watch?v=yCQN096CwWM&ab_channel=TusharRoy-CodingMadeSimple

# Sorted list that supporting add/update in O(logN) time
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        l = r = 0
        ans = float("-inf")
        # sum of each row from column l to column r
        for l in range(n):
            dp = [0] * m
            for r in range(l, n):
                # given retangle with left and right position
                # use kadane algorithm to find top and bottom
                for row in range(m):
                    dp[row] += matrix[row][r]

                rec = self.kadane(dp)  # O(n)
                if rec < k:
                    ans = max(ans, rec)
                elif rec == k:
                    return k
                else:
                    # if max subarray sum is larger than k, find the largest smaller than k O(nlogn)
                    sl = SortedList([0])
                    s = 0
                    for num in dp:
                        s += num
                        # existing prefix sum need to be at least s-k so that
                        # subarray sum <= k
                        largest_smaller = sl.bisect_left(s - k)
                        if largest_smaller < len(sl):
                            # print(s, sl[largest_smaller], s - sl[largest_smaller])
                            ans = max(ans, s - sl[largest_smaller])

                        sl.add(s)

        return ans

    def kadane(self, arr: list[int]) -> int:
        ans = float("-inf")
        s = 0  # max ending at i

        for num in arr:
            s = max(s + num, num)
            ans = max(ans, s)

        return ans
