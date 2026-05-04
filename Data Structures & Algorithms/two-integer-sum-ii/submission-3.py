class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if h[temp]:
                return [h[temp],i+1]
            h[numbers[i]] = i + 1
        return []

        