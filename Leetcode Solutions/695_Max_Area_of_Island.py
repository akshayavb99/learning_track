"""
Question link - https://leetcode.com/problems/max-area-of-island/description/
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen=set()
        m,n = len(grid), len(grid[0])

        def dfs(row,col):
            if row<0 or row>=m or col<0 or col>= n:
                return 0
            
            if grid[row][col]==0 or (row,col) in seen:
                return 0
            
            seen.add((row,col)) 
            return (1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row, col-1))
        
        maxArea = 0
        for r in range(m):
            for c in range(n):
                maxArea = max(maxArea, dfs(r,c))
        
        return maxArea
                
        
