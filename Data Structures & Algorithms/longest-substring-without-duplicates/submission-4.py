class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = 0
        maxst = 0
        for c in range(len(s)):
            if s[c] in h:
                l = max(h[s[c]]+1,l)
            h[s[c]] = c
            maxst = max(maxst,c-l+1)
        return maxst        