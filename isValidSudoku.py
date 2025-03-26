class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            if not self.is_valid_block(row):
                return False
            
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_block(column):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [
                    board[box_row + r][box_col + c]
                    for r in range(3)
                    for c in range(3)
                ]
                if not self.is_valid_block(box):
                    return False
        return True

    def is_valid_block(self,block):
        seen = set()
        for num in block:
            if num != ".":
                if num in seen:
                    return False
                seen.add(num)   
        return True
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
print(solution.isValidSudoku(board))