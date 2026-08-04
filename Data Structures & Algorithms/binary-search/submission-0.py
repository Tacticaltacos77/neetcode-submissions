class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        out = -1
        while l < r:
            m = (r-l)//2 + l
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                out = m
                break
        if nums[l] == target:
            out=l
        return out
            
