class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        storage = {0 : 1}
        res = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            diff = cur - k
            res += storage.get(diff, 0)
            storage[cur] = 1 + storage.get(cur, 0)
        return res