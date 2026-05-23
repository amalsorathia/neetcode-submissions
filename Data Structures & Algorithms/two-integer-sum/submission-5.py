class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        index = {}
    
        for i in range(0, len(nums)):
            
            complement = target - nums[i]
            
            # comp[complement] = i
            
            
            if complement in index:
                return [index[complement], i]
                
            index[nums[i]] = i
        
