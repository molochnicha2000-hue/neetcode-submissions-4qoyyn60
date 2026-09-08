class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        def binary(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        l, r = 0, N - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1

        pivot = (l + r) // 2
        print(pivot)
        first = binary(0, pivot)
        if first != -1:
            return first
        return binary(pivot + 1, N - 1)

        
