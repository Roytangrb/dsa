# Author: RT
# Date: 2023-07-23T18:19:33.685Z
# URL: https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/


import heapq


class Solution:
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        # minimum total count of nums to form the kth group is
        # consecutive sequence of 1..k
        usageLimits.sort()
        nums = usageLimits
        n = len(nums)

        total = 0  # running total prefix nums frequency
        k = 1  # length of next group attempt
        for num in nums:
            total += num
            if total >= (k + 1) * k // 2:
                k += 1

        return k - 1

    def maxIncreasingGroups__max_heap(self, usageLimits: list[int]) -> int:
        # O(n^2logn) TLE using max heap
        mh = [-ul for ul in usageLimits]
        heapq.heapify(mh)
        k = 1
        ans = 0
        while len(mh) >= k:
            ans += 1
            used = []
            for _ in range(k):
                left = -heapq.heappop(mh) - 1
                if left:
                    used.append(left)
            for left in used:
                heapq.heappush(mh, -left)

            k += 1

        return ans
