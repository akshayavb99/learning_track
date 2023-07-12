'''
Question link - https://leetcode.com/problems/permutations/description/
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def dfs():
            #print (subset)
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    dfs()
                    subset.pop()
        
        dfs()
        return result
            
            
