# Author: RT
# Date: 2023-09-24T05:37:37.279Z
# URL: https://leetcode.com/problems/beautiful-towers-ii/description/

# Similar:
# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        stack = [(maxHeights[0], 1)]
        s = maxHeights[0]
        for i in range(1, n):
            curr = maxHeights[i]
            left[i] = s
            curr_w = 1
            while stack and stack[-1][0] > curr:
                top, w = stack.pop()
                delta = (top - curr) * w
                left[i] -= delta
                s -= delta
                curr_w += w

            s += curr
            stack.append((curr, curr_w))

        right = [0] * n
        stack = [(maxHeights[-1], 1)]
        s = maxHeights[-1]
        for i in range(n - 2, -1, -1):
            curr = maxHeights[i]
            right[i] = s
            curr_w = 1
            while stack and stack[-1][0] > curr:
                top, w = stack.pop()
                delta = (top - curr) * w
                right[i] -= delta
                s -= delta
                curr_w += w

            s += curr
            stack.append((curr, curr_w))

        return max(maxHeights[i] + left[i] + right[i] for i in range(n))
