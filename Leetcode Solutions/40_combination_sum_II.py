'''
Question link - https://leetcode.com/problems/combination-sum-ii/
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        subset = []

        def dfs(idx, target):
            if target<0:
                return

            if target == 0:
                result.append(subset.copy())
                return
            
            prev=-1
            for i in range(idx,len(candidates)):
                if candidates[i] == prev:
                    continue
                #Option 1- Add elemen in current index idx
                subset.append(candidates[i])
                dfs(i+1, target-candidates[i])

                #Option 2 - Don't add element in current index idx
                subset.pop()
                prev=candidates[i]
        
        dfs(0,target)
        return result
