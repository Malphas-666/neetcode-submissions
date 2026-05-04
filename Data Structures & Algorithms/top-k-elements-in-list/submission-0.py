class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = set()
        dic = {}
        for i in nums:
            if i not in seen:
                seen.add(i)
                dic[i] = 1
            else:
                dic[i] +=1
        l = []
        for i in range(k):
            m = max(dic,key=dic.get)
            l.append(m)
            dic.pop(m)
        return l

