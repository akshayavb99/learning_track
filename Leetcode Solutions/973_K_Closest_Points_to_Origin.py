'''
Question link - https://leetcode.com/problems/k-closest-points-to-origin/description/
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        result = []
        dist = [[x*x + y*y, x,y] for [x,y] in points]
        heapq.heapify(dist)
        print(dist)

        while k>0:
            [d, x,y] = heapq.heappop(dist)
            result.append([x,y])
            k-=1
        
        return result
