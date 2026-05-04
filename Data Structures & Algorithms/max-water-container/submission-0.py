class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        mw = (min(heights[l],heights[r]))*(r-l)
        while l!=r:
            if heights[l]<heights[r]:
                l+=1
                mw= max(mw,(min(heights[l],heights[r]))*(r-l))
            else:
                r-=1
                mw= max(mw,(min(heights[l],heights[r]))*(r-l))
        
        return mw

        