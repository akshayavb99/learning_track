'''
Question link - https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-n for n in nums]
        heapq.heapify(nums)
        i=0
        print(nums)

        while i<k:
            rem = heapq.heappop(nums)
            if i==k-1:
                return -rem
            i+=1
        
        return -1

        
