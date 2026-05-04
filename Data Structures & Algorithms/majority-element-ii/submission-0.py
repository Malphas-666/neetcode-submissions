class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] +=1
            else:
                h[i] = 1
        l = []
        for j in h:
            if h[j] > len(nums)/3:
                l.append(j)
        return l
        
        