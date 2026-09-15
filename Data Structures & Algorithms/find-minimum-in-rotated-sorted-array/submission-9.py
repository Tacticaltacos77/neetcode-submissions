class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l<=r:
            m = (r-l) // 2 + l
            res = min(nums[m], res)
            if nums[l] <= nums[r]:
                return min(nums[l], res)
            elif nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1