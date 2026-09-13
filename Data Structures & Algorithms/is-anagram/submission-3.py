class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for c in s:
            sd[c]+=1
        for c in t:
            if c in sd:
                sd[c]-=1
                if sd[c]==0:
                    sd.pop(c)
            else:
                return False
        return len(sd) ==0