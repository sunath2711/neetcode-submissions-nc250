class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                row_str = f"{val} in row {i}"
                col_str = f"{val} in col {j}"
                grid_str = f"{val} in box {i // 3}-{j // 3}"

                if row_str in seen or col_str in seen or grid_str in seen:
                    return False
                seen.add(row_str)
                seen.add(col_str)
                seen.add(grid_str)
        
        return True





        