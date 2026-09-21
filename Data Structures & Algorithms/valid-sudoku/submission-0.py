class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows = len(board)
        # cols = len(board[0])

        # check rows for duplicates
        for row in range(0,9):
            seen = set()
            for col in range(0,9):
                if board[row][col]=='.':
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])


        # check cols for duplicates
        for col in range(0,9):
            seen = set()
            for row in range(0,9):
                if board[row][col]=='.':
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])


        # check all 3x3 boxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col]=='.':
                        continue
                    if board[row][col]in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True



        


        