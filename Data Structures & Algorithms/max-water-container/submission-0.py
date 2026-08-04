class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out =0
        temp =0
        l, r = 0, len(heights)-1
        while l<r:
            if heights[l] > heights[r]:
                wl = heights[r]
            else:
                wl = heights[l]
            temp = wl * (r-l)
            if r-l-1 ==0 and wl > out:
                out = wl
            elif out <temp:
                out=temp
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return out