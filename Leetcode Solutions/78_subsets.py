'''
Question link: https://leetcode.com/problems/subsets/description/
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        subset = []

        def dfs(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return
            
            #Option 1: Include current index element in subset
            subset.append(nums[idx])
            dfs(idx+1)

            #Option 2: Do not include current index element in subset
            subset.pop()
            dfs(idx+1)
        
        dfs(0)
        return result
