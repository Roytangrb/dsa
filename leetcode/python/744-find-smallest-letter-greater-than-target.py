# Author: RT
# Date: 2023-06-09T03:43:05.435Z
# URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/


import bisect


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]
