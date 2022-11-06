class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = []
        others = []
        
        for i in range(len(nums)-1):
            
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
            if nums[i] == 0:
                zeros.append(0)
            else:               
                others.append(nums[i])
            
            if i == len(nums)-2:
                # for the last one
                if nums[-1] == 0:
                    zeros.append(0)
                else:               
                    others.append(nums[-1])
                
        return others+zeros