class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for i in nums:
            if i in num:
                return True
                break
            else:
                num.add(i)
            
        return False 
        