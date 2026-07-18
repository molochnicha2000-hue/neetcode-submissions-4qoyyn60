class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        storage = {0 : -1}
        current = 0
        for i, x in enumerate(nums):
            current += x
            remain = current % k
            if remain not in storage:  
                storage[remain] = i

            elif i - storage[remain] > 1:
                return True

        return False
        
        
        