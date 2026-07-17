class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total = nums.count(k)
        res = 0
        for i in range(1, 51):
            if i == k:
                continue
            cnt = 0
            for x in nums:
                if x == i:
                    cnt += 1
                if x == k:
                    cnt -= 1
                cnt = max(cnt, 0)
                res = max(res, cnt + total)
        return res