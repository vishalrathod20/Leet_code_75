from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_map = defaultdict(int)  # Dictionary to store frequency of each row's representation
        count = 0
        
        # Step 1: Convert each row to a tuple and store its frequency in row_map
        for row in grid:
            row_map[tuple(row)] += 1
            
        # Step 2: For each column, create a tuple representation and check in row_map
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_map:
                count += row_map[col_tuple]
                
        return count
