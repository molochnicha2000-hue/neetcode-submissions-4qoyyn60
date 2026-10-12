class Solution:
    def insert(self, arr: List[List[int]], new: List[int]) -> List[List[int]]:
        arr = sorted(arr + [new])
        res = []
        cur = arr[0]
        for i in range(1, len(arr)):
            new = arr[i]
            if new[0] > cur[1]:
                res.append(cur)
                cur = new
            else:
                cur[1] = max(cur[1], new[1])
        return res + [cur]