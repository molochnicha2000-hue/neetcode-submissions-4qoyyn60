class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)

        l, r = 0, N - 1
        start = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                start = min(start, m)
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = 0, N - 1
        end = float('-inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                end = max(end, m)
                l = m + 1              
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        if start == float('inf'):
            return [-1, -1]
        return [start, end]
