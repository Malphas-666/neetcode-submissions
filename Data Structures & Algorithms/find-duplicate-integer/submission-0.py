class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = set()
        for i in nums:
            if i in h:
                return i
            else:
                h.add(i)