'''
Question link - https://leetcode.com/problems/last-stone-weight/description/
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            #print(stones)
            num1,num2 = heapq.heappop(stones),heapq.heappop(stones)
            print(num1,num2)
            if num1!=num2:
                heapq.heappush(stones,num1-num2)
            #print(stones)
            #print()
        
        if len(stones)==1:
            return stones[0]*-1
        else:
            return 0
