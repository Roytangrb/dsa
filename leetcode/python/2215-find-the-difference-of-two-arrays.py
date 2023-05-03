# Author: RT
# Date: 2023-05-03T04:58:24.218Z
# URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
