class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = collections.Counter(nums)
        res = []
        N = len(nums)

        for value, freq in f.items():
            if freq > N // 3:
                res.append(value)
        # sorting staff
        return res