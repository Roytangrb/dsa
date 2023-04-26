# Author: RT
# Date: 2023-04-26T02:16:45.119Z
# URL: https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        # brute force
        while num > 9:
            num = sum(map(int, str(num)))

        return num

    def digital_root(self, num: int) -> int:
        """Digital root formula
        https://en.wikipedia.org/wiki/Digital_root
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9

        return num % 9
