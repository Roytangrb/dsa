# Author: RT
# Date: 2022-08-02T16:04:15.350Z
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        # linear search to count elements in matrix <= value
        # and return the largest element <= value
        def count_lte(value):
            i, j = 0, n - 1
            count = 0
            smaller = matrix[0][0]  # largest <= value
            larger = matrix[-1][-1]  # smallest >= value
            while i < n and j >= 0:
                if matrix[i][j] > value:
                    larger = min(larger, matrix[i][j])
                    j -= 1
                else:
                    smaller = max(smaller, matrix[i][j])
                    count += j + 1
                    i += 1

            return count, smaller, larger

        # [top-left, top-right] corners is the range
        # binary search on range, determine sizes of [left, mid], O(nlog(max-min))
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = l + (r - l) // 2
            count, smaller, larger = count_lte(mid)
            # the matrix could contain duplicate numbers,
            # cannot increment/decrement mid directly
            if count > k:
                r = smaller
            elif count < k:
                l = larger
            else:
                return smaller

        return l
