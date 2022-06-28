# Author: RT
# Date: 2022-06-28T15:20:19.089Z
# URL: https://leetcode.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for _ in range(n)]
        col_used = set()
        diag_used = set()
        anti_diag_used = set()
        ans = []

        def backtrack(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                diag_id = r - c
                anti_diag_id = r + c
                if (
                    c not in col_used
                    and diag_id not in diag_used
                    and anti_diag_id not in anti_diag_used
                ):
                    col_used.add(c)
                    diag_used.add(diag_id)
                    anti_diag_used.add(anti_diag_id)
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
                    col_used.remove(c)
                    diag_used.remove(diag_id)
                    anti_diag_used.remove(anti_diag_id)

        backtrack(0)

        return ans
