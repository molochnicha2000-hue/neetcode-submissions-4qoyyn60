class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        res = []
        curNum, count = nums[0], 1
        for i in range(1, N):
            if curNum == nums[i]:
                count += 1
            else:
                if count > N // 3:
                    res.append(curNum)
                curNum = nums[i]
                count = 1
        if count > N // 3:
            res.append(curNum)
        return res