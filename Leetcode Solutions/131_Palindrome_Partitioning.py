'''
Question link - https://leetcode.com/problems/palindrome-partitioning/description/
'''

class Solution:
    def dfs(self, idx, s, subset):
        if idx >= len(s):
            self.result.append(subset.copy())
            return
        
        for j in range(idx, len(s)):
            if s[idx:j+1]==''.join(reversed(s[idx:j+1])):
                subset.append(s[idx:j+1])
                self.dfs(j+1,s,subset)
                subset.pop()
        
        return

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(0,s,[])
        return self.result
    
    
