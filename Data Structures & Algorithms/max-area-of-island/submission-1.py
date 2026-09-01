class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row, col, res = None):

            if not res:
                res = []
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[row]):
                return
            if grid[row][col] == 0:
                return

            grid[row][col] = 0

            res.append((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, res)
            return res
            

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if grid[row][col] == 1:
                    res = dfs(row, col, res = [])
                    max_area = max(max_area, len(res))
        return max_area
        