class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3 loops one for row, col and then grid 3x3
        
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
        
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in col_set:
                    return False
                col_set.add(board[i][j])

        for box_r in range(0,9,3):
            for box_c in range(0,9,3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_r + i][box_c + j]
                        if val == ".":
                            continue
                        elif val in box_set:
                            return False
                        box_set.add(val)


        return True



        