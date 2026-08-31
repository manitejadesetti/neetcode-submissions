class Solution:
    

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, res = None):
            if not res:
                res = []
            if row < 0 or row >= len(grid):
                return

            if col < 0 or col >= len(grid[row]):
                return
            
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"

            res.append([row, col])

            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            return res
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count