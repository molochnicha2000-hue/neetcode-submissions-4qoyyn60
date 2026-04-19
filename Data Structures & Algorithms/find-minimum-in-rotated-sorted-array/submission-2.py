class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        minRes = float("inf")
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] < minRes:
                minRes = nums[mid]
            
            if nums[mid] > nums[r]:       
                l = mid + 1 
            else: #nums[mid] < nums[r]:
                # if nums[mid] > nums[r] -> l = mid + 1
                r = mid - 1
            #else:

        return minRes
        