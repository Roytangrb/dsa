# Author: RT
# Date: 2022-06-07T12:48:09.065Z
# URL: https://leetcode.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            k = i + j + 1
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
