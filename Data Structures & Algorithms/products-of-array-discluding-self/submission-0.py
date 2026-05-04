class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            pr = 1
            for j in range(len(nums)):
                if i != j:
                    pr *= nums[j]
            l.append(pr)
            
        
        return l