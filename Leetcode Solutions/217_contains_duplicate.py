class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        track = {}

        for n in nums:
            if n in track:
                return True
            track[n]=1
        
        return False
        
