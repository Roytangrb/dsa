# Author: RT
# Date: 2023-05-24T04:02:10.842Z
# URL: https://leetcode.com/problems/maximum-subsequence-score/


import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # score is determined by min of subset nums2 with size of k
        # sort while maintain relative order, iterate nums2 from largest to
        # smallest. When nums2[i] is the min, subset of nums1 elements could
        # be picked from prefix (inclusive).
        n = len(nums1)
        pairs = sorted(zip(nums2, nums1), reverse=True)

        min_heap = [p[1] for p in pairs[:k]]
        heapq.heapify(min_heap)
        s = sum(min_heap)
        ans = s * pairs[k - 1][0]
        for i in range(k, n):
            if pairs[i][1] > min_heap[0]:
                s = s + pairs[i][1] - min_heap[0]
                heapq.heapreplace(min_heap, pairs[i][1])

            ans = max(ans, s * pairs[i][0])

        return ans
