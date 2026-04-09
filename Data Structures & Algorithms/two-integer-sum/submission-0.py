class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = {}
        for n in range(len(nums)):
            need_n = target - nums[n]
            if need_n in numsSet:
                return [numsSet[need_n], n] 

            numsSet[nums[n]] = n 
        
        return