class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hesh = set(nums)
        count = 0
        
        for i in hesh:
            if(i - 1) not in hesh:
                length = 1
                while(i+length) in hesh:
                    length += 1
                count = max(length ,count)
        return count
        