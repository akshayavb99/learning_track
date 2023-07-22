'''
Question link - https://leetcode.com/problems/number-of-islands/description/
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m,n=len(grid),len(grid[0])

        def dfs(row,col):
            grid[row][col]="-1"

            if row<m-1 and grid[row+1][col]=='1':
                dfs(row+1, col)
            
            if row>0 and grid[row-1][col]=='1':
                dfs(row-1,col)
            
            if col<n-1 and grid[row][col+1]=='1':
                dfs(row,col+1)
            
            if col>0 and grid[row][col-1]=='1':
                dfs(row,col-1)
        
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        
        return count
