class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            n = nums[i]
            while l < r:
                summa = n + nums[l] + nums[r]
                if summa == 0:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
                elif summa > 0:
                    r -= 1
                else:
                    l += 1

            
        return res


        