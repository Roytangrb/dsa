# Author: RT
# Date: 2022-12-18T10:26:01.142Z
# URL: https://leetcode.com/problems/daily-temperatures/


from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = deque()
        for i, temp in enumerate(reversed(temperatures)):
            while stack and temp >= stack[-1][0]:
                stack.pop()

            ans.appendleft(i - stack[-1][1] if stack else 0)
            stack.append((temp, i))

        return list(ans)
