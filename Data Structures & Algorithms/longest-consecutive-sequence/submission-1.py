class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hesh = set(nums)
        count = 0
        
        for i in hesh:
            flag = True
            new_count = 1
            while flag:
                
                if i+1 in hesh:
                    new_count +=1
                    i +=1
                else:
                    if count< new_count:
                        count = new_count
                    flag = False
        return count
        