class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # find pivot
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = r
        pivot1 = r
        print(pivot)
        print(pivot1)

        def bin_s(left, right):
            while left <= right:
                midd = (left + right) // 2
                if nums[midd] == target:
                    return midd
                
                if nums[midd] > target: 
                    right = midd- 1
                else:
                    left = midd + 1
            return -1

        result = bin_s(0, pivot - 1)
        if result != -1: return result

        result = bin_s(pivot, len(nums) - 1)
        if result != -1: return result
        return -1
                
        