'''
Question link - https://leetcode.com/problems/combination-sum/description/
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result=[]
        subset=[]

        def dfs(idx,curVal):
            print(idx,curVal)
            if curVal > target or idx >= len(candidates):
                return
            
            if curVal==target:
                result.append(subset.copy())
                #print("Found")
                return
            
            #Option 1: Current index is included
            subset.append(candidates[idx])
            dfs(idx, curVal+candidates[idx])

            #Option 2: Current index is not included
            subset.pop()
            dfs(idx+1, curVal)   
        
        dfs(0,0)

        return result
