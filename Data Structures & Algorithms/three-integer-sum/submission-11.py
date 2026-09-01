class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = set()

        for i in range(N):
            cur = nums[i]
            j, k = i + 1, N - 1
            while j < k:
                if cur + nums[j] + nums[k] == 0:
                    res.add((cur, nums[j], nums[k]))
                    prev = j
                    while j <= k and nums[j] == nums[prev]:
                        j += 1
                    continue
                    
                if cur + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return [list(x) for x in res]
