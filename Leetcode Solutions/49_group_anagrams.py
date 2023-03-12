#Question: https://leetcode.com/problems/group-anagrams/description/

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i)-ord('a')]+=1
            
            answer[tuple(count)].append(s)
        return list(answer.values())
      
'''
Time Complexity = O(M*N), N = Number of strings, M = Maximum length of string 
Space Complexity = O(26*N + M*N) = O(M*N), N = Number of strings, M = Maximum length of string. Note that count array of length 26 is created newly for every string
'''
            
