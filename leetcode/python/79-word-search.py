# Author: RT
# Date: 2022-11-24T15:10:00.856Z
# URL: https://leetcode.com/problems/word-search/


from collections import Counter
from functools import cache
from itertools import chain


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        bc = Counter(chain(*board))
        if bc[word[-1]] > bc[word[0]]:
            word = word[::-1]

        if len(word) > m * n:
            return False

        if len(set(word)) > len(bc.keys()):
            return False

        # 1 <= m, n <= 6
        def pos(i: int, j: int) -> int:
            return 1 << (i * n + j)

        @cache
        def dfs(i: int, j: int, k: int, mask: int) -> bool:
            if k == len(word):
                return True

            if 0 <= i < m and 0 <= j < n:
                cur = pos(i, j)
                if not (mask & cur) and board[i][j] == word[k]:
                    mask |= cur
                    ret = (
                        dfs(i + 1, j, k + 1, mask)
                        or dfs(i - 1, j, k + 1, mask)
                        or dfs(i, j + 1, k + 1, mask)
                        or dfs(i, j - 1, k + 1, mask)
                    )
                    return ret

            return False

        return any(dfs(i, j, 0, 0) for i in range(m) for j in range(n))
