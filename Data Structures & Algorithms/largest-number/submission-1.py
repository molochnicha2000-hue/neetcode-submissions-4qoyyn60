class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        res = []
        while arr:
            max_n = 0
            for i in range(1, len(arr)):
                if arr[i] + arr[max_n] > arr[max_n] + arr[i]:
                    max_n = i
            res.append(arr[max_n])
            arr.pop(max_n)
        return "".join(res) if res[0] != "0" else "0"