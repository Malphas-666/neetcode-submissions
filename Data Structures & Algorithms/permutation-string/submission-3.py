class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def dictt():
            h = {}
            for i in range(len(s1)):
                h[s1[i]] = h.get(s1[i],0)+1
            return h
        h = dictt()
        m = len(s1)-1
        r = 0
        for l in range(len(s2)):
            if s2[l] in h:
                h[s2[l]] -=1
                while r<m:
                    if l+2 > len(s2):
                        return False
                    if s2[l+1] in h and h[s2[l+1]] != 0:
                        h[s2[l+1]]-=1
                        l+=1
                        r+=1
                    else:
                        r = 0
                        h = dictt()
                        break
                else:
                    return True
        return False


            

        