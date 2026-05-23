class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # calculate the complement of each num in array
        # make a hashmap of each number and its index for easy access
        # check if complement is in num hashmap, if it is return its index
        # question: is the array always ordered ?
        # bc the larger number won't be in the array until later, want
        # to return the complement index first and then the current #
        numMap = {}
        for i in range(0, len(nums)):
            
            complement = target - nums[i] 
            if complement in numMap:
                return [numMap.get(complement), i]
            # add number AFTER the check bc that way don't have to do the whole
            # if numMap.get(complement) != i then return
            numMap[nums[i]] = i