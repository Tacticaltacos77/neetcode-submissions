class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        chars = defaultdict(int)
        avail = k 
        out = 0
        currS = 0
        largest = ""
        while r <len(s):
            chars[s[r]]+=1
            currS+=1
            if largest=="":
                largest =s[r]
            elif chars[largest] < chars[s[r]]:
                largest = s[r]
            if currS - chars[largest] <= k:
                out = max(currS, out)
            else:
                currS-=1
                chars[s[l]]-=1
                l+=1
            r+=1
            
            
        return out
                