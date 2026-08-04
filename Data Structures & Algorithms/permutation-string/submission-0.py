class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        out = False
        freqSub = defaultdict(int)
        for c in s1:
            freqSub[c]+=1
        while r < len(s2):
            freq = defaultdict(int)
            substring = s2[l:r+1]
            for char in substring:
                freq[char] += 1
            if freq == freqSub:
                return True
            l += 1
            r += 1
        return out