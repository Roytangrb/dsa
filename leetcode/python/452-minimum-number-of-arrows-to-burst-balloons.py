# Author: RT
# Date: 2023-01-05T14:28:53.401Z
# URL: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """Begin shooting from the front"""
        ans = 0
        points.sort(key=lambda x: tuple(x))  # start asc, end asc
        points = iter(points)
        window = next(points)

        def _intersection(a: list[int], b: list[int]) -> tuple[bool, list[int]]:
            if b[0] > a[1]:
                return False, []
            else:
                return True, [b[0], min(a[1], b[1])]

        for point in points:
            overlap, new_window = _intersection(window, point)
            if not overlap:
                ans += 1
                window = point
            else:
                window = new_window

        return ans + 1

    def findMinArrowShots2(self, points: list[list[int]]) -> int:
        """Shoot backwards"""
        points.sort(key=lambda x: x[1])
        n = len(points)
        ans = 0

        shoot = float("-inf")
        np = 0
        while np < n:
            if not (points[np][0] <= shoot <= points[np][1]):
                shoot = points[np][1]
                ans += 1
            np += 1

        return ans
