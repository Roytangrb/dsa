# Author: RT
# Date: 2023-01-08T12:56:01.444Z
# URL: https://leetcode.com/problems/max-points-on-a-line/


from collections import Counter
from fractions import Fraction


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """O(n3) 2 points determine a straight line
        naive checking all points on every possible line
        """
        n = len(points)
        ans = 1
        cache = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    if x1 not in cache:
                        cache.add(x1)
                        ans = max(ans, sum(1 for x, _ in points if x == x1))
                else:
                    k = Fraction(y1 - y2, x1 - x2)
                    b = y1 - k * x1
                    if (k, b) not in cache:
                        cache.add((k, b))
                        ans = max(ans, sum(1 for x, y in points if y == k * x + b))

        return ans

    def maxPoints__map(self, points: list[list[int]]) -> int:
        """O(n2) Point and slope determine a straight line"""
        n = len(points)
        ans = 1
        for i in range(n - 1):
            slopes = Counter()
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                k = float("inf") if x1 == x2 else Fraction(y1 - y2, x1 - x2)
                slopes[k] += 1

            ans = max(ans, max(slopes.values()) + 1)

        return ans
