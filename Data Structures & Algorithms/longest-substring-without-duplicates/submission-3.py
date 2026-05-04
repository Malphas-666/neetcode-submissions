class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        l = 0
        maxst = 0
        for c in range(len(s)):
            while s[c] in h:
                h.remove(s[l]) 
                l+=1
            h.add(s[c])
            maxst = max(maxst,c-l+1)
        return maxst        