# Author: RT
# Date: 2022-11-23T13:10:02.730Z
# URL: https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            seenc = [False] * 10
            seenr = [False] * 10
            seeng = [False] * 10
            for j in range(9):
                cell = board[j][i]
                if cell != ".":
                    cell = int(cell)
                    if seenc[cell] is True:
                        return False
                    seenc[cell] = True

                cell = board[i][j]
                if cell != ".":
                    cell = int(cell)
                    if seenr[cell] is True:
                        return False
                    seenr[cell] = True

                gr, gc = divmod(j, 3)
                offr, offc = divmod(i, 3)
                gr += offr * 3
                gc += offc * 3

                cell = board[gr][gc]
                if cell != ".":
                    cell = int(cell)
                    if seeng[cell] is True:
                        return False
                    seeng[cell] = True

        return True
