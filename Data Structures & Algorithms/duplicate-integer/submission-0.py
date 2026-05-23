class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         set = {}
         for i in range(0, len(nums)):
            if nums[i] in set.values():
                return True
            set[i] = nums[i]
        
         return False