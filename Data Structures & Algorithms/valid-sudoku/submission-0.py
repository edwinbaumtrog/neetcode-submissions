from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row, arr in enumerate(board):
            for col, value in enumerate(arr):
                if not value.isnumeric():
                    continue

                lessrow = board[row].copy()
                lessrow.pop(col)

                if value in lessrow:
                    return False

                s = set()
                for i in range(len(board)):
                    if not board[i][col].isnumeric():
                        continue

                    if board[i][col] in s:
                        return False

                    s.add(board[i][col])

                t = set()
                box_row = (row // 3) * 3
                box_col = (col // 3) * 3

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if not board[i][j].isnumeric():
                            continue

                        if board[i][j] in t:
                            return False

                        t.add(board[i][j])

        return True