# Author: RT
# Date: 2022-12-24T09:22:41.810Z
# URL: https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        M = 1_000_000_007

        if n < 2:
            return n

        even = [0] * (n + 1)  # last column filled with 2 grids
        odd = [0] * (n + 1)  # last column filled with 1 grid

        even[1] = 1
        even[2] = 2
        odd[2] = 2

        for i in range(3, n + 1):
            even[i] = (even[i - 1] + even[i - 2] + odd[i - 1]) % M
            odd[i] = (odd[i - 1] + even[i - 2] * 2) % M

        return even[n]
