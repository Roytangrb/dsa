# Author: RT
# Date: 2023-06-27T00:11:29.212Z
# URL: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        # Example: nums1 = [1, 7, 11]; nums2 = [2, 4, 6]
        #   1 7 11
        # 2 a b e
        # 4 b c
        # 6 c d
        # Going down or right gets pair with larger sum. After pick from smallest pair from
        # candidate min-heap, add the pair below and the pair to the right to candidate heap
        m, n = len(nums1), len(nums2)
        q = [(nums1[0] + nums2[0], 0, 0)]
        seen = {(0, 0)}
        ans = []
        count = min(m * n, k)
        while count:
            _sum, i, j = heapq.heappop(q)
            ans.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in seen:
                heapq.heappush(q, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in seen:
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))

            count -= 1

        return ans

    def kSmallestPairs__brute_force(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        # O(mn * log(k))
        q = []
        for num1 in nums1:
            for num2 in nums2:
                if len(q) < k:
                    heapq.heappush(q, (-num1 - num2, [num1, num2]))
                elif num1 + num2 < -q[0][0]:
                    heapq.heapreplace(q, (-num1 - num2, [num1, num2]))

        return [i[1] for i in q]
