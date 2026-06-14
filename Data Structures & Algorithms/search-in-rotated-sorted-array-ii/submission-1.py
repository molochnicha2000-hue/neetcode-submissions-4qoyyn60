class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        return target in nums
        N = len(nums)
        if nums[0] < nums[-1]:
            l, r = 0, N - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return True
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
        else:
            l, r = 0, N - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return True
                if nums[0] < nums[m] and nums[m] > target:
                    l = m + 1
                else:
                    r = m - 1
            return False