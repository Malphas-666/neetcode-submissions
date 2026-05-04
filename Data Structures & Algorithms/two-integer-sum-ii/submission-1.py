class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hesh = {}
        for i,num in enumerate(numbers, start=1):
            hesh[num] = i
        for i,num in enumerate(numbers, start=1):
            diff = target - num
            if diff in hesh and hesh[diff] != i:
                return[i,hesh[diff]]
        