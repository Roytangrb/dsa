# Author: RT
# Date: 2022-07-18T16:05:58.952Z
# URL: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/


from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        a = self.build_2d_prefix(matrix)
        ans = 0
        for x1 in range(m):
            for x2 in range(x1, m):
                # width [x1, x2] is fixed, compress height to 1D problem
                # similar to https://leetcode.com/problems/subarray-sum-equals-k/
                seen_prefix_sum_count = Counter()
                seen_prefix_sum_count[0] = 1
                # count submatrix right bound ending at y
                for y in range(n):
                    s = self.query_submatrix_sum(a, x1, 0, x2, y)
                    ans += seen_prefix_sum_count.get(s - target, 0)
                    seen_prefix_sum_count[s] += 1

        return ans

    def build_2d_prefix(self, M: list[list[int]]) -> list[list[int]]:
        m, n = len(M), len(M[0])
        a = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not i and not j:
                    a[i][j] = M[i][j]
                elif not i:
                    a[i][j] = M[i][j] + a[i][j - 1]
                elif not j:
                    a[i][j] = M[i][j] + a[i - 1][j]
                else:
                    a[i][j] = M[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

        return a

    def query_submatrix_sum(
        self, a: list[list[int]], x1: int, y1: int, x2: int, y2: int
    ) -> int:
        if not x1 and not y1:
            return a[x2][y2]
        elif not x1:
            return a[x2][y2] - a[x2][y1 - 1]
        elif not y1:
            return a[x2][y2] - a[x1 - 1][y2]

        return a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]
