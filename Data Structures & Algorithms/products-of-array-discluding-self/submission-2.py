class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        zeros = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
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
            elif zeros == 0:
                n = int(s/nums[i])    
            else:
                n = 0
            out.append(n)

        return out