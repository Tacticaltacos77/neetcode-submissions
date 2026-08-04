class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxS =0
        currS =0
        subS = set()
        while r<len(s):
            if s[r] not in subS:
                subS.add(s[r])
                currS+=1
                r+=1
            else:
                subS.remove(s[l])
                l+=1
                currS-=1
                

            maxS = max(maxS, currS)
        return maxS