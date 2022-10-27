# Author: RT
# Date: 2022-10-27T14:40:16.474Z
# URL: https://leetcode.com/problems/image-overlap/


class Solution:
    """Shift and count using bitset

    Other approaches:
        1. Linear representation of sparse matrix
        2. Convolution https://en.wikipedia.org/wiki/Kernel_(image_processing)
    """

    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)  # 1 <= n <= 30
        bs1, bs2 = [], []
        for r in range(n):
            row1 = row2 = 0
            for c in range(n):
                row1 = row1 << 1 | img1[r][c]
                row2 = row2 << 1 | img2[r][c]

            bs1.append(row1)
            bs2.append(row2)

        return self.overlap(bs1, bs2)

    def overlap(self, bs1: list[int], bs2: list[int]) -> int:
        # simulate img1 translated, fix img2 position
        n = len(bs1)
        ans = 0
        for translate_x in range(1 - n, n):
            left = translate_x < 0
            right = not left
            for translate_y in range(1 - n, n):
                up = translate_y < 0
                down = not up
                overlap = 0
                if down:
                    for r in range(n - translate_y):
                        r1 = (
                            bs1[r] >> translate_x
                            if right
                            else bs1[r] << abs(translate_x)
                        )
                        r2 = bs2[r + translate_y]
                        # overlap += "{0:b}".format(r1 & r2).count("1")
                        overlap += (r1 & r2).bit_count()  # requires 3.10+
                else:
                    for r in range(abs(translate_y), n):
                        r1 = (
                            bs1[r] >> translate_x
                            if right
                            else bs1[r] << abs(translate_x)
                        )
                        r2 = bs2[r - abs(translate_y)]
                        overlap += (r1 & r2).bit_count()

                ans = max(ans, overlap)

        return ans
