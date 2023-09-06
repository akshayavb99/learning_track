"""
Question link - https://leetcode.com/problems/pacific-atlantic-water-flow/description/
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m,n=len(heights),len(heights[0])
        result=set()
        pac, atl = set(),set()


        def dfs(r,c,seen,prevHeight):
            if r<0 or r>=m or c<0 or c>=n or ((r,c)) in seen or heights[r][c]<prevHeight:
                return
            seen.add((r,c))      
            dfs(r+1,c,seen,heights[r][c])
            dfs(r-1,c,seen,heights[r][c]) 
            dfs(r,c+1,seen,heights[r][c]) 
            dfs(r,c-1,seen,heights[r][c])       
            


        for r in range(m):
            #Pacific ocean cells
            dfs(r,0,pac,heights[r][0])

            #Atlantic ocean cells
            dfs(r,n-1,atl,heights[r][n-1])
        
        for c in range(n):
            #Pacific ocean cells
            dfs(0,c,pac,heights[0][c])

            #Atlantic ocean cells
            dfs(m-1,c,atl,heights[m-1][c])
        
        for (r,c) in pac:
            if (r,c) in atl:
                result.add((r,c))
        
        return result
             
                
