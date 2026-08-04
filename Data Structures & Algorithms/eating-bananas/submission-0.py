class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        out = r
        while l <= r:
            k = (r+l)//2
            hours = 0
            for p in piles:
                hours += p //k
                if p%k !=0:
                    hours+=1
            if hours<=h:
                out = min(out, k)
                r=k-1
            else:
                l = k+1
        return out