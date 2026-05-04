class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)>1:
            i,j = 0,1
            def sort(i,j,nums):
                while j <= len(nums)-1:
                    if nums[i]> nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        j +=1
                    else:
                        j +=1
                i +=1
                j = i+1
                if i == len(nums)-1:
                    return nums
                sort(i,j,nums)
            sort(i,j,nums)
        

        
        