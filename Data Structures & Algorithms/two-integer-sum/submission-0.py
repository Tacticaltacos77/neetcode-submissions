class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in dic:
                return [dic[tar], i]
            dic[nums[i]] = i
            
            

