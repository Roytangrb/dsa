# Author: RT
# Date: 2022-09-29T12:20:57.135Z
# URL: https://leetcode.com/problems/find-k-closest-elements/


import bisect
from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """Binary search + sliding window"""
        n = len(arr)
        i = bisect.bisect_left(arr, x)
        l = i - 1
        r = i

        ans = deque()
        while k:
            diff_l = float("inf") if l < 0 else abs(arr[l] - x)
            diff_r = float("inf") if r == n else abs(arr[r] - x)

            if diff_l <= diff_r:
                ans.appendleft(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1

            k -= 1

        return list(ans)
