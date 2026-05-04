class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,n in enumerate(nums):
            h[n]=i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in h and h[diff]!=i:
                return [i,h[diff]]

                