# Author: RT
# Date: 2022-08-20T14:07:19.167Z
# URL: https://leetcode.com/problems/split-array-into-consecutive-subsequences/


import heapq


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        # min-heap last value, length of sequence
        seqs = []
        for num in nums:
            # filter current sequences that cannot be extended
            while seqs and seqs[0][0] + 1 < num:
                _, length = heapq.heappop(seqs)
                if length < 3:
                    return False

            if not seqs or seqs[0][0] == num:  # start new sequence
                heapq.heappush(seqs, (num, 1))
            else:  # extend shortest sequence
                heapq.heapreplace(seqs, (num, seqs[0][1] + 1))

        return all(length >= 3 for _, length in seqs)
