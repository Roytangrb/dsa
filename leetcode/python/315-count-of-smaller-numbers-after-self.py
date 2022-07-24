# Author: RT
# Date: 2022-07-24T13:03:03.808Z
# URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/


import sys

sys.path.append("src")

from data_structures.segment_tree import SegmentTree


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        st = SegmentTree(20001)

        for i in range(n - 1, -1, -1):
            bucket = nums[i] + 10000
            st.update(bucket, st.get(bucket) + 1)
            ans[i] = st.sum_range(0, bucket - 1)

        return ans
