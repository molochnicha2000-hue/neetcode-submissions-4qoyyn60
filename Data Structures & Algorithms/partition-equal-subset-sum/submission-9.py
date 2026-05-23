class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        N = len(nums)
        target = sum(nums) // 2
        
        visit = set()
        visit.add(0)
        for i in range(N - 1, -1, -1):
            cur = nums[i]
            new = set([i for i in visit])
            new.add(cur)
            for j in visit:
                n = cur + j
                if n == target:
                    return True
                new.add(n)

            visit = new
        return False
        

        