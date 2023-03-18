class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        freqs = {i:[] for i in range(len(nums)+1)}
        answer=[]

        for n in nums:
            count[n]=count.get(n,0)+1
        
        for num, countVal in count.items():
            freqs[countVal].append(num)

        for i in range(len(nums),0,-1):
            for j in freqs[i]:
                answer.append(j)
                if len(answer)==k:
                    return answer 
            
'''
Time complexity: O(N) - N = Length of nums array
Space complexity: O(N)
'''
