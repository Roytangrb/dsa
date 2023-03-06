# Author: RT
# Date: 2023-03-06T12:54:31.752Z
# URL: https://leetcode.com/problems/kth-missing-positive-number/


from itertools import chain


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            missing = arr[mid] - mid - 1
            if missing < k:
                l = mid + 1
            else:
                r = mid

        return l + k

    def brute_force(self, arr: list[int], k: int) -> int:
        prev = 0
        for num in chain(arr, [float("inf")]):
            gap = num - prev - 1
            if k > gap:
                k -= gap
            else:
                return prev + k

            prev = num

        return -1
