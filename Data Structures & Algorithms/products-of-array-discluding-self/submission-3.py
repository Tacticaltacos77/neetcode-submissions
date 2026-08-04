class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        zeros = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
                if zeros >1:
                    return [0] *len(nums)
            elif s==0:
                s+=nums[i]
            else:
                s*=nums[i]
           
        for i in range(len(nums)):
            if zeros ==1:
                if nums[i]!=0:
                    n = 0
                else:
                    n = s
            else:
                n = int(s/nums[i])    
            
            out.append(n)

        return out