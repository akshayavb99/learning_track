class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftProd = [1 for i in range(len(nums))]
        rightProd = [1 for i in range(len(nums))]
        result = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            leftProd[i] = leftProd[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1,-1):
            rightProd[i] = rightProd[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = leftProd[i] * rightProd[i]

        return result
      
  
 """
 Time complexity = O(3*N) = O(N), N - Lenth of array nums
 Space complexity = O(3*N) = ON)
 """
        
