class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        for i in range(N):
            cur = nums[i]
            for j in range(i + 1, N):
                if cur == nums[j] and abs(j - i) <= k:
                    return True
        return False