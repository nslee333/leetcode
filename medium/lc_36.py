import unittest
from collections import defaultdict

"""
Leetcode 36 Valid Sudoku

"""

class Solution:
    def isValidSudoku(self, board) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r /3, c/3) -> integer division
       
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3 , c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


class Test(unittest.TestCase):        
    def test(self):
        s = Solution()
        
        input = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        expected = True
        output = s.isValidSudoku(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        expected = False
        output = s.isValidSudoku(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()