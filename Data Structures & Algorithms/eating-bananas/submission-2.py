class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        rate = 0
        while l<=r:
            mid = (l+r)//2
            count = 0
            for i in piles:
                count += i//mid + (1 if i%mid!= 0 else 0)
            if count <=h:
                rate = mid
                r=mid-1
            else:
                l=mid+1
        return rate
            
        
        