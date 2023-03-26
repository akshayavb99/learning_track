class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        track = {}

        for i in range(len(nums)):
            if target-nums[i] in track:
                return [i, track[target-nums[i]]]
            
            track[nums[i]]=i
        
        return [-1,-1]

"""
Time complexity: O(N), N - Length of nums
Space complexity: O(N)
"""
