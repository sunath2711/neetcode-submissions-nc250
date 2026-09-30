class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                row_str = str(val) +" in row" + str(i)
                col_str = str(val) +" in col" + str(j) 
                grid_str = str(val) +" in grid" + str(i//3) + str(j//3)

                if row_str in seen or col_str in seen or grid_str in seen:
                    return False

                seen.add(row_str)
                seen.add(col_str)
                seen.add(grid_str)

        return True
        

        