class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setLen = set(nums)
        return len(setLen) != len(nums) 