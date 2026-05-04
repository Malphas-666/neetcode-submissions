class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h = set(nums)
        for i in range(len(h)+1):
            if i+1 not in h:
                return i+1
        