class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        track={}

        for ch in s:
            track[ch] = track.get(ch,0)+1
        
        for ch in t:
            if ch not in track or track[ch]<=0:
                return False
            else:
                track[ch] = track[ch]-1
        
        return True
      
'''
Time complexity = O(2M) = O(M), M = Length of s and t
Space complexity = O(M) 
'''
        
