class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        #res = collections.defaultdict(list)
        res = {}

        for i in range(min(nums), max(nums) + 1):
            res[i] = []
        
        for n in nums:
            res[n].append(n)
        
        ans = []
        for j, arr in res.items():
            for i in arr:
                ans.append(i)
        
        return ans